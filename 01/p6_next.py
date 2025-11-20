from ib111 import week_01  # noqa
from math import ceil, sqrt


# Napište funkci, která pro zadané celé číslo ‹number›
# najde nejbližší větší číslo, které je násobkem kladného
# celého čísla ‹k›.

def next_multiple(number, k):
    divisor = number/float(k)
    if number % k == 0:
        return number + k
    return k * ceil(divisor)


# Dále napište funkci, která pro zadané kladné celé číslo
# ‹number› najde nejbližší větší prvočíslo.

def next_prime(number):
    if number < 2:
        return 2
    if number < 3:
        return 3
    i = number + 1
    while True:
        if i % 2 != 0 and i % 3 != 0:
            divided = False
            for k in range(3, (ceil(sqrt(i))) + 1, 2):
                if i % k == 0:
                    divided = True
                    break
            if not divided:
                return i
        i += 1


def main():
    assert next_multiple(1, 2) == 2
    assert next_multiple(10, 7) == 14
    assert next_multiple(10, 5) == 15
    assert next_multiple(54, 6) == 60
    assert next_multiple(131, 29) == 145
    assert next_multiple(123, 112) == 224
    assert next_multiple(423, 90) == 450

    assert next_prime(1) == 2
    assert next_prime(2) == 3
    assert next_prime(3) == 5
    assert next_prime(4) == 5
    assert next_prime(11) == 13
    assert next_prime(12) == 13
    assert next_prime(13) == 17
    assert next_prime(23) == 29


if __name__ == "__main__":
    main()
