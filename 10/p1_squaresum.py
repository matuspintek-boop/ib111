from ib111 import week_10  # noqa
import math


# Napište predikát, který rozhodne, zda lze dané číslo ‹num› napsat
# jako součet ⟦∑ᵢ₌₁ⁿaᵢ²⟧, kde ⟦n⟧ je zadáno parametrem ‹count› a
# ⟦aᵢ⟧ jsou po dvou různá kladná čísla. Jinými slovy, lze ‹num›
# zapsat jako součet ‹count› druhých mocnin různých kladných čísel?

def remaining_sum(list_: list[int]) -> int:
    sum_: int = 0
    for item in list_:
        sum_ += item
    return sum_


def helper(total: int, last_used: int, remaining: int, num: int) -> bool:
    if remaining == 0:
        return total == num
    if total > num:
        return False

    i_max = math.isqrt(num - total)

    max_possible = remaining_sum([(i_max - k)**2 for k in range(remaining)])
    if total + max_possible < num:
        return False

    for i in range(last_used + 1, i_max + 1):
        if helper(total + i*i, i, remaining - 1, num):
            return True
    return False


def is_sum_of_squares(num: int, count: int) -> bool:

    return helper(0, 0, count, num)


def main() -> None:
    assert is_sum_of_squares(42, 3)
    assert not is_sum_of_squares(42, 2)
    assert not is_sum_of_squares(18, 2)
    assert not is_sum_of_squares(100, 3)
    assert is_sum_of_squares(100, 5)
    assert not is_sum_of_squares(1000, 13)


if __name__ == '__main__':
    main()
