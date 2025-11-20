from ib111 import week_03  # noqa


# Naprogramujte (čistou) funkci, která ze dvou vzestupně seřazených
# seznamů čísel ‹a›, ‹b› vytvoří nový vzestupně seřazený seznam,
# který bude obsahovat všechny prvky z ‹a› i ‹b›. Nezapomeňte, že
# nesmíte modifikovat vstupní seznamy (jinak by funkce nebyla
# čistá). Pokuste se funkci naprogramovat «efektivně».

def merge(a, b):

    # starting indexes of a, b
    i = 0
    j = 0

    # early exit
    if len(a) == 0:
        return b
    if len(b) == 0:
        return a

    output = []
    # for each cycle, each item of list before its index is already added,
    # working only with not added items, always adding the smaller item
    # and incresing thew index of it's list (parent-list)
    while len(output) < len(a) + len(b):
        if j < len(b) and i < len(a):
            if b[j] <= a[i]:
                output.append(b[j])
                j += 1
            else:
                output.append(a[i])
                i += 1
            continue

        if j == len(b):
            output.append(a[i])
            i += 1
            continue

        output.append(b[j])
        j += 1
    return output


def main():
    assert merge([1, 2, 3], [1, 2, 3]) == [1, 1, 2, 2, 3, 3]
    assert merge([0, 2, 4, 6, 8], [1, 3, 5, 7, 9]) \
        == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert merge([], []) == []
    assert merge([], [1, 2]) == [1, 2]
    assert merge([1, 2], []) == [1, 2]
    assert merge([1, 5, 10], [-1, 2, 3, 4, 6, 10, 11]) \
        == [-1, 1, 2, 3, 4, 5, 6, 10, 10, 11]


if __name__ == "__main__":
    main()
