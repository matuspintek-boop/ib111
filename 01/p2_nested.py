from ib111 import week_01  # noqa


# Napište funkci ‹nested›, která spočítá ‹n›-tý člen posloupnosti
# (počítáno od 0), která vznikne napojením postupně se
# prodlužujících prefixů přirozených čísel.
#
# Nechť ⟦Aᵢ⟧ je posloupnost čísel ⟦1⟧ až ⟦i⟧:
#
#  ⟦ A₁ → 1
#    A₂ → 1, 2
#    A₃ → 1, 2, 3
#    A₄ → 1, 2, 3, 4
#    A₅ → 1, 2, 3, 4, 5 ⟧
#
# Hledaná posloupnost ⟦B⟧ vznikne napojením posloupností ⟦A₁⟧, ⟦A₂⟧,
# ⟦A₃⟧ … (do nekonečna) za sebe:
#
#  ⟦ B  → 1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, … ⟧
#
# Vaším úkolem je najít ‹n›-tý prvek posloupnosti ⟦B⟧.

def find_index_of_last_one(index, n):
    addition = 1
    while index < n:
        if index + addition <= n:
            index += addition
            addition += 1
        else:
            break

    return index


def nested(n):
    last_one = find_index_of_last_one(0, n)
    return 1 + (n - last_one)


# Dále napište funkci ‹nested_sum›, která spočítá sumu prvních ‹n› členů
# této posloupnosti.

def my_sum(n):
    sum_ = 0
    last_added = 0
    last_addition = 0
    addition = 1
    index = -1
    while index != n:
        if index + addition <= n:
            index += addition
            addition += 1
            last_added += 1
            sum_ += last_addition + last_added
            last_addition += last_added
            continue
        for i in range(n-index):
            sum_ += i+1
            index = n
    return sum_


def nested_sum(n):
    return my_sum(n-1)


def main():
    assert nested(0) == 1
    assert nested(1) == 1
    assert nested(2) == 2
    assert nested(8) == 3
    assert nested(9) == 4
    assert nested(25) == 5
    assert nested(130) == 11

    assert nested_sum(2) == 2
    assert nested_sum(5) == 7
    assert nested_sum(13) == 26
    assert nested_sum(30) == 87
    assert nested_sum(100) == 500


if __name__ == "__main__":
    main()
