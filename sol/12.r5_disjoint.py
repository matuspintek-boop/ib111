def to_digits(n: int) -> list[int]:
    if n == 0:
        return [0]
    out = []
    while n > 0:
        out.append(n % 10)
        n //= 10
    return out


def from_digits(digits: list[int]) -> int | None:
    if not digits:
        return None
    out = 0
    for d in digits:
        out *= 10
        out += d
    return out


def nearest_disjoint(n: int) -> int | None:
    digits = to_digits(n)
    available = set(range(10)) - set(digits)
    tail_len = len(digits) - 1

    if not available:
        return None

    first = digits[-1]
    big_digit = max(available)
    small_digit = min(available)
    small_nonzero = 0 if available == {0} else min(available - {0})

    first_small = [x for x in available if x < first]
    first_big = [x for x in available if x > first]

    lead_small = [max(first_small)] if first_small else []
    lead_big = [min(first_big)] if first_big else [small_nonzero, small_digit]

    tail_big = [big_digit for i in range(tail_len)]
    tail_small = [small_digit for i in range(tail_len)]
    smaller = from_digits(lead_small + tail_big)
    bigger = from_digits(lead_big + tail_small)

    if smaller is not None and bigger is not None and n - smaller < bigger - n:
        return smaller
    return bigger
