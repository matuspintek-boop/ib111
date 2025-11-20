from ib111 import week_08  # noqa

# Napište čistou funkci ‹local_extremes›, která dostane na vstupu
# seznam ‹values› čísel a vrátí dvojici seznamů ‹min_indices,
# max_indices›. Každý prvek seznamu ‹values› je unikátní. Seznam
# ‹min_indices› (‹max_indices›) bude obsahovat indexy lokálních
# minim (maxim) seznamu ‹values›. Oba tyto seznamy budou vzestupně
# seřazené. Řešení očekáváme v lineární časové složitosti.

Minima = list[int]
Maxima = list[int]


def local_extremes(values: list[int]) -> tuple[Minima, Maxima]:
    minima: Minima = []
    maxima: Maxima = []

    if len(values) == 0 or len(values) == 1:
        if len(values) == 1:
            minima.append(0)
            maxima.append(0)
        return minima, maxima

    for i in range(len(values)):
        if i == 0:
            if values[i] < values[i+1]:
                minima.append(i)
            if values[i] > values[i+1]:
                maxima.append(i)
            continue

        if i == len(values) - 1:
            if values[i] < values[i-1]:
                minima.append(i)
            if values[i] > values[i-1]:
                maxima.append(i)
            continue

        if values[i] > values[i-1] and values[i] > values[i+1]:
            maxima.append(i)
        if values[i] < values[i-1] and values[i] < values[i+1]:
            minima.append(i)

    return minima, maxima


def main() -> None:
    assert local_extremes([1, 4, 2, 0]) == ([0, 3], [1])
    assert local_extremes([3, 1, 5, 4, 0, 2]) == ([1, 4], [0, 2, 5])
    assert local_extremes([3, 1, 5, 6, 0, 2]) == ([1, 4], [0, 3, 5])
    assert local_extremes([3, 1, 0]) == ([2], [0])
    assert local_extremes([0, 1, 2]) == ([0], [2])
    assert local_extremes([]) == ([], [])
    assert local_extremes([2]) == ([0], [0])
    assert local_extremes([1, 2]) == ([0], [1])


if __name__ == "__main__":
    main()
