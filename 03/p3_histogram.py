from ib111 import week_03  # noqa


# Napište (čistou) funkci, která pro zadaný seznam nezáporných čísel
# ‹data› vrátí nový seznam obsahující dvojice – číslo a jeho
# četnost. Výstupní seznam musí být seřazený vzestupně dle první
# složky. Můžete předpokládat, že v ‹data› se nachází pouze celá
# čísla z rozsahu [0, 100] (včetně).

def histogram(data):
    if len(data) == 0:
        return []
    minimum = min(data)
    maximum = max(data)
    record = [0 for i in range(maximum+1 - minimum)]
    output = []

    for digit in data:
        record[digit-minimum] += 1

    for index, data_ in enumerate(record):
        if data_ > 0:
            output.append((index+minimum, data_))

    return output


def main() -> None:
    assert histogram([1, 2, 3, 2, 1]) == [(1, 2), (2, 2), (3, 1)]
    assert histogram([7, 1, 7, 1, 5]) == [(1, 2), (5, 1), (7, 2)]
    assert histogram([1, 1, 1]) == [(1, 3)]
    assert histogram([]) == []
    assert histogram([1000000]) == [(1000000, 1)]


if __name__ == "__main__":
    main()
