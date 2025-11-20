

class FinStream:
    def __init__(self, data: list[int]) -> None:
        self.data = data
        self.pos = 0

    def take_head(self) -> tuple[int | None, 'Stream']:
        if self.pos >= len(self.data):
            return (None, self)

        tail = FinStream(self.data)
        tail.pos = self.pos + 1
        return (self.data[self.pos], tail)


class Cycle:
    def __init__(self, inner: 'Stream') -> None:
        self.inner = inner
        self.orig = inner

    def take_head(self) -> tuple[int | None, 'Stream']:
        tail = Cycle(self.orig)
        head, tail.inner = self.inner.take_head()
        if head is None:
            head, tail.inner = self.orig.take_head()
        return (head, tail)


class Drop:
    def __init__(self, n: int, inner: 'Stream') -> None:
        self.inner = inner
        for _ in range(n):
            _, self.inner = self.inner.take_head()

    def take_head(self) -> tuple[int | None, 'Stream']:
        return self.inner.take_head()


class Take:
    def __init__(self, n: int, inner: 'Stream') -> None:
        self.n = n
        self.inner = inner

    def take_head(self) -> tuple[int | None, 'Stream']:
        if self.n == 0:
            return None, self

        tail = Take(self.n - 1, self.inner)
        head, tail.inner = self.inner.take_head()
        return (head, tail)


class Skip:
    def __init__(self, inner: 'Stream', skips: 'Stream') -> None:
        self.inner = inner
        self.skips = skips

    def take_head(self) -> tuple[int | None, 'Stream']:
        head, inner_tail = self.inner.take_head()
        skip, skips_tail = self.skips.take_head()

        if skip is not None:
            for _ in range(skip):
                head_skipped, inner_tail = inner_tail.take_head()

        return (head, Skip(inner_tail, skips_tail))


Stream = FinStream | Cycle | Drop | Take | Skip


def to_stream(data: list[int]) -> Stream:
    return FinStream(data.copy())


def cycle(stream: Stream) -> Stream:
    return Cycle(stream)


def drop(n: int, original: Stream) -> Stream:
    return Drop(n, original)


def take(n: int, original: Stream) -> Stream:
    return Take(n, original)


def skip(inner: Stream, skips: Stream) -> Stream:
    return Skip(inner, skips)
