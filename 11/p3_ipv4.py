from ib111 import week_11  # noqa


# V této úloze se budeme zabývat adresami protokolu IP verze 4,
# které sestávají ze 4 čísel oddělených tečkami, například
# ‹192.0.2.0› (více informací o IPv4 naleznete například na
# Wikipedii). Adresy budeme reprezentovat řetězci.

# Napište predikát, kterého hodnota bude ‹True›, představuje-li jeho
# parametr validní IPv4 adresu. Daná IPv4 adresa je validní právě
# tehdy, když je tvořená čtyřmi dekadickými čísly od 0 až 255
# (včetně) oddělenými tečkou (pro jednoduchost v této úloze
# připouštíme pouze kanonický tvar IPv4 adres).

def convert(string: str) -> int:
    data: dict[str, int] = {"0": 0, "1": 1, "2": 2, "3": 3,
                            "4": 4, "5": 5, "6": 6, "7": 7,
                            "8": 8, "9": 9}
    output: int = 0

    for char in string:
        output *= 10
        output += data[char]
    return output


def ipv4_validate(address: str) -> bool:
    partial_masks: list[str] = address.split(".")
    if len(partial_masks) != 4:
        return False
    for substring in partial_masks:
        if not (substring.isdecimal() and (-1 < convert(substring) < 256)):
            return False
    return True


# Dále napište čistou funkci, která vypočte číselnou hodnotu dané
# adresy.  Konverze IPv4 adresy na její číselnou hodnotu je podobná
# konverzi binárního zápisu čísla na dekadický s tím rozdílem, že
# u IPv4 adresy pracujeme se základem 256. Hodnota adresy
# ‹192.0.2.0› je tedy ⟦192⋅256³ + 0⋅256² + 2⋅256¹ + 0⋅256⁰ =
# 3 221 225 984⟧. Můžete počítat s tím, že vstupem bude vždy validní
# IPv4 adresa ve výše popsaném kanonickém tvaru.

def ipv4_value(address: str) -> int:
    partial_masks: list[str] = address.split(".")
    output: int = 0

    partial_masks.reverse()

    for index, value in enumerate(partial_masks):
        output += convert(value)*256**index
    return output


def main() -> None:
    assert ipv4_validate("192.0.2.0")
    assert ipv4_validate("5.5.5.5")
    assert ipv4_validate("255.255.255.255")
    assert ipv4_validate("0.0.0.0")
    assert not ipv4_validate("a.5.5.5")
    assert not ipv4_validate("0.0.0.č")
    assert not ipv4_validate("256.4.3.2")
    assert not ipv4_validate("1.2.3.-1")
    assert not ipv4_validate("2.2.2.")
    assert not ipv4_validate("2.2.2")
    assert not ipv4_validate("5.5.5.5.5")

    assert ipv4_value("192.0.2.0") == 3221225984
    assert ipv4_value("0.0.0.0") == 0
    assert ipv4_value("255.255.255.255") == 4294967295
    assert ipv4_value("1.1.1.1") == 16843009
    assert ipv4_value("12.0.55.200") == 201340872


if __name__ == "__main__":
    main()
