class Stream:
    def __init__(self, data: list[int]) -> None:
        self.data = data
        self.pos = 0
        self.step = 1

    def get(self) -> int:
        elem = self.data[self.pos]
        self.pos = (self.pos + self.step) % len(self.data)
        return elem


def cycle(data: list[int]) -> Stream:
    return Stream(data.copy())


def drop(n: int, original: Stream) -> Stream:
    stream = Stream(original.data.copy())
    stream.step = original.step
    stream.pos = (original.pos + n * stream.step) % len(stream.data)
    return stream


def take(n: int, original: Stream) -> list[int]:
    result = []
    for _ in range(n):
        result.append(original.get())
    return result


def every_nth(n: int, original: Stream) -> Stream:
    stream = Stream(original.data.copy())
    stream.pos = original.pos
    stream.step = (original.step * n) % len(original.data)
    return stream
