from ib111 import week_10  # noqa


# Napište čistou funkci, která ze vstupního seznamu vytvoří seznam
# všech jeho permutací (tedy seznamů takových, že jsou tvořena
# stejnými hodnotami v libovolném pořadí). Výsledný seznam permutací
# nechť je uspořádán lexikograficky.

# Nápověda: řešení se znatelně zjednoduší, budete-li celou dobu
# pracovat se seřazenou verzí vstupního seznamu (seřazení je nakonec
# také jen permutace). Dobré řešení pak vytvoří každou permutaci
# pouze jednou a také je vytvoří rovnou ve správném pořadí.
def my_permutations(word: list[int]) -> list[list[int]]:
    if len(word) == 0:
        return [[]]
    if len(word) == 1:
        return [word]
    else:
        item: int = word.pop()
        output: list[list[int]] = []
        for combination in my_permutations(word):
            for i in range(len(combination)+1):
                new_combination: list[int] = combination.copy()
                new_combination.insert(i, item)
                output.append(new_combination)
        return output


def unique(data: list[list[int]]) -> list[list[int]]:
    output: list[list[int]] = []
    output.append(data[0])
    for i in range(1, len(data)):
        if output[-1] != data[i]:
            output.append(data[i])

    return output


def permutations(word: list[int]) -> list[list[int]]:
    sorted_word: list[int] = sorted(word)

    return unique(sorted(my_permutations(sorted_word)))


def main() -> None:
    assert permutations([]) == [[]]
    assert permutations([1, 1]) == [[1, 1]]
    assert permutations([1, 2]) == [[1, 2], [2, 1]]
    assert permutations([3, 1, 2]) == [[1, 2, 3],
                                       [1, 3, 2],
                                       [2, 1, 3],
                                       [2, 3, 1],
                                       [3, 1, 2],
                                       [3, 2, 1]]


if __name__ == '__main__':
    main()
