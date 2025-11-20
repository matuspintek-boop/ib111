from ib111 import week_04  # noqa


# Napište čistou funkci, která na vstupu dostane dvě celá kladná
# čísla ‹rows› a ‹cols› a vrátí tabulku (dvourozměrný seznam)
# o ‹rows› řádcích a ‹cols› sloupcích. V buňce v řádku ‹y› a sloupci
# ‹x› bude počet společných dělitelů čísel ‹x› a ‹y›. Levý horní roh
# má souřadnice ‹x = y = 1›.

# Například pro vstup ‹rows = 4›, ‹cols = 2› dostaneme tabulku ‹[[1,
# 1], [1, 2], [1, 1], [1, 2]]›.

# funkcia gcd pre ziskanie najvacie spolocneho delitela cisel a a b, a >= b
def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


# pocet spolocnych delitelov a, b sa rovna poctu delitolov gcd(a, b)
def number_of_divisors(a: int) -> int:
    divisors: int = 1
    for i in range(1, a // 2 + 1):
        if a % i == 0:
            divisors += 1

    return divisors


def common_divisors(rows: int, cols: int) -> list[list[int]]:
    output: list[list[int]] = []

    for i in range(rows):
        row: list[int] = []
        for j in range(cols):
            biggest_divisor: int = gcd(i+1, j+1)
            total_divisors: int = number_of_divisors(biggest_divisor)
            row.append(total_divisors)
        output.append(row)
    return output


def main() -> None:
    assert common_divisors(4, 2) == [[1, 1], [1, 2], [1, 1], [1, 2]]
    assert common_divisors(1, 1) == [[1]]
    assert common_divisors(1, 8) == [[1, 1, 1, 1, 1, 1, 1, 1]]
    assert common_divisors(5, 1) == [[1], [1], [1], [1], [1]]
    assert common_divisors(6, 6) == [[1, 1, 1, 1, 1, 1],
                                     [1, 2, 1, 2, 1, 2],
                                     [1, 1, 2, 1, 1, 2],
                                     [1, 2, 1, 3, 1, 2],
                                     [1, 1, 1, 1, 2, 1],
                                     [1, 2, 2, 2, 1, 4]]
    assert common_divisors(2, 4) == [[1, 1, 1, 1],
                                     [1, 2, 1, 2]]


if __name__ == '__main__':
    main()
