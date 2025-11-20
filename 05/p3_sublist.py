from ib111 import week_05  # noqa


# V tomto příkladu dostanete dva seznamy obsahující celá čísla.
# Vaším úkolem je napsat čistou funkci ‹largest_common_sublist_sum›,
# která najde takový společný podseznam seznamů ‹left› a ‹right›,
# který má největší celkový součet, a tento součet vrátí.

# Podseznamem seznamu ‹S› myslíme takový seznam ‹T›, pro který
# existuje číslo ‹k› takové, že platí ‹S[k + i] == T[i]› pro všechna
# ‹i› taková, že ⟦0 ≤ i < len(T)⟧. Například seznam ‹[1, 2]› je
# podseznamem seznamu ‹[0, 1, 2, 3]›, kde ‹k = 1›.

# Složitost smí být v nejhorším případě až kubická vzhledem k délce
# delšího vstupního seznamu.

def find_sequence(i: int, j: int, max_list: list[int],
                  min_list: list[int]) -> int:
    sum_: int = 0
    highest: int = 0

    while i < len(max_list) \
        and j < len(min_list) \
            and max_list[i] == min_list[j]:
        sum_ += max_list[i]
        i += 1
        j += 1
        highest = max(sum_, highest)

    return highest


def largest_common_sublist_sum(left: list[int], right: list[int]) -> int:
    largest_sum: int = 0

    max_list: list[int] = left if len(left) >= len(right) else right
    min_list: list[int] = right if len(right) <= len(left) else left

    for i in range(len(max_list)):
        value = max_list[i]
        for j in range(len(min_list)):
            if min_list[j] == value:
                candidate: int = find_sequence(i, j, max_list, min_list)
                if candidate > largest_sum:
                    largest_sum = candidate

    return largest_sum


def main() -> None:
    l1: list[int] = []
    l2 = [1, 2, 3, 4, 5]
    l3 = [2, 3, 4, 6, 7, 9, 10]
    l4 = [1, 2, 3, 8, 9]

    A = [3, -1, 4, 2, 5, -2, 6]
    B = [4, 2, 5]

    assert largest_common_sublist_sum(l1, l2) == 0
    assert largest_common_sublist_sum(l2, l3) == 9
    assert largest_common_sublist_sum(l2, l4) == 6
    assert largest_common_sublist_sum(l3, l4) == 9
    assert largest_common_sublist_sum(B, A) == 11


if __name__ == "__main__":
    main()
