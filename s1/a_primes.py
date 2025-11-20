from ib111 import week_01  # noqa
from math import ceil, sqrt


# Napište čistou funkci ‹nth_smallest_prime_divisor›, která vrátí ‹index›-té
# nejmenší prvočíslo vyskytující se v prvočíselném rozkladu čísla ‹num›.
# Pokud se v rozkladu vyskytuje některé prvočíslo vícekrát, počítáme všechny
# jeho výskyty, tedy např. v čísle ⟦2 · 2 · 3 · 3 · 3 · 5 = 540⟧ je třetím
# nejmenším prvočíslem číslo 3. Pokud má ‹num› méně než ‹index› prvočísel
# v rozkladu, funkce vrátí ‹None›.
#
# Předpokládejte, že ‹num› i ‹index› jsou kladná celá čísla.
# Zde indexujeme od 1, tedy první prvočíslo v rozkladu má ‹index› 1.
#
# Je potřeba, aby vaše funkce fungovala rozumně rychle i pro velmi velká
# čísla, u nichž je hledané prvočíslo malé. (Není třeba vymýšlet zvláště
# chytrá řešení, jen je třeba nedělat zbytečnou práci navíc.)


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


def nth_smallest_prime_divisor(num, index):
    # setting starting values

    current_prime = 2
    counter = index

    # cycle that declines counter, and always finds new prime,
    # if current is no longer divisor

    while num > 1 and counter > 0:
        if num % current_prime == 0:
            num //= current_prime
            counter -= 1
        else:
            current_prime = next_prime(current_prime)
            continue

    if num == 1 and counter > 0:
        return
    return current_prime


def main():
    assert nth_smallest_prime_divisor(20, 1) == 2
    assert nth_smallest_prime_divisor(42350, 2) == 5
    assert nth_smallest_prime_divisor(42350, 3) == 5
    assert nth_smallest_prime_divisor(42350, 4) == 7
    assert nth_smallest_prime_divisor(42350, 7) is None


if __name__ == '__main__':
    main()
