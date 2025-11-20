from math import pi


def degrees(radians: float) -> float:
    return (radians * 180) / pi


def diagonal(lst: list[list[int]]) -> list[int]:
    diag = []
    for i in range(len(lst)):
        diag.append(lst[i][i])
    return diag


def to_list(num: int, base: int) -> list[int]:
    digits = []
    result = []

    while num > 0:
        digits.append(num % base)
        num //= base

    for i in range(len(digits)):
        result.append(digits[-i - 1])

    return result


Element = tuple[int, str]


def with_id(elements: list[Element], id_: int) -> str | None:
    for element_id, val in elements:
        if id_ == element_id:
            return val
    return None


Student = tuple[int, str, int | None]


def update_students(students: list[Student],
                    end: int) -> list[Student]:

    result: list[Student] = []

    for uco, name, graduated in students:
        if graduated is None:
            graduated = end
        result.append((uco, name, graduated))

    return result


def is_increasing(seq: list[int]) -> bool:
    for i in range(1, len(seq)):
        if seq[i - 1] >= seq[i]:
            return False
    return True
