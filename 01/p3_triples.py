from ib111 import week_01  # noqa
from math import sqrt, isqrt


# Napište funkci ‹largest_triple›, která najde pythagorejskou
# trojici ⟦(a, b, c)⟧ – totiž takovou, že ⟦a⟧, ⟦b⟧ a ⟦c⟧ jsou
# přirozená čísla a platí ⟦a² + b² = c²⟧ (tzn. tvoří pravoúhlý
# trojúhelník). Hledáme trojici, která:
#
#  1. má největší možný součet ⟦a + b + c⟧,
#  2. hodnoty ⟦a⟧, ⟦b⟧ jsou menší než ‹max_side›.
#
# Výsledkem funkce bude součet ⟦a + b + c⟧, tedy největší možný
# obvod pravoúhlého trojúhelníku, jsou-li obě jeho odvěsny kratší
# než ‹max_side›. Předpokládejte, že ‹max_side› bude vždy alespoň 5.

def largest_triple(max_side):
    current_sum = 0
    for i in range(max_side - 1, 0, -1):
        for j in range(i, 0, -1):
            prepona = i**2 + j**2
            x = isqrt(prepona)
            if current_sum > i + j + x:
                break

            if isqrt(prepona) == sqrt(prepona):
                current_sum = i + j + x
                break
    return current_sum


def main():
    assert largest_triple(10) == 24
    assert largest_triple(25) == 72
    assert largest_triple(100) == 288
    assert largest_triple(150) == 490
    assert largest_triple(1000) == 3290


if __name__ == "__main__":
    main()
