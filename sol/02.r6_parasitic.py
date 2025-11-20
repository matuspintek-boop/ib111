from typing import Annotated


def is_parasitic(num: nat1, base: int) -> 'int | None':
    orig = num
    last = num % base
    power = 1
    while num >= base:
        power *= base
        num //= base
    new = orig // base + last * power
    return new // orig if new % orig == 0 else None
