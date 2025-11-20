from ib111 import week_02  # noqa


# Napište funkci, která vytvoří číslo zřetězením ‹count› po sobě
# jdoucích kladných čísel počínaje zadaným číslem ‹start›.  Tato
# čísla zřetězte vyjádřená v binární soustavě. Například volání
# ‹joined(1, 3)› zřetězí sekvenci ⟦(1)₂ = 1⟧, ⟦(10)₂ = 2⟧, ⟦(11)₂ = 3⟧
# a vrátí číslo ⟦(11011)₂ = 27⟧. V Pythonu lze binární čísla přímo
# zapisovat v tomto tvaru: ‹0b11011› (podobně lze stejné číslo
# zapsat v šestnáctkové soustavě zápisem ‹0x1b› nebo osmičkové jako
# ‹0o33›).

def joined(start, count):
    record = 0
    output = 0
    i = 0

    # converting number to binary
    while count > 0:
        start_ = start
        converted = 0
        index = 0

        while start_ > 0:
            current = start_ % 2
            converted += current * 10 ** index
            index += 1
            start_ //= 2

        record *= 10 ** index
        record += converted

        start += 1
        count -= 1

    # converting binary to output sum
    while record > 0:
        current = record % 10
        output += current * 2 ** i
        i += 1
        record //= 10

    return output


def main() -> None:
    assert joined(1, 3) == 0b11011
    assert joined(10, 4) == 0b1010101111001101
    assert joined(8, 5) == 0b10001001101010111100
    assert joined(99, 2) == 0b11000111100100
    assert joined(999, 3) == 0b111110011111111010001111101001
    assert joined(1111, 1) == 0b10001010111


if __name__ == "__main__":
    main()
