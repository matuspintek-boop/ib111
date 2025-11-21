from ib111 import week_12  # noqa


# Napište čistou funkci ‹restore_sequence›, která dostane neprázdný řetězec
# složený pouze z číslic 0 a 1 a vrátí množinu všech možných
# řetězců, které vzniknou doplněním znaků čárky ‹','› do původního
# řetězce tak, aby části jimi oddělené byly dvojkové zápisy čísel
# v intervalu od ‹low› do ‹high› včetně. Hodnota ‹low› bude vždy
# alespoň 1. Rozdělení musí být takové, že žádný zápis neobsahuje
# levostranné nuly.


# convert int to binary str
def num_to_binstr(num: int, convertor: list[str]) -> str:
    output: str = ""
    while num > 0:
        output = convertor[num % 2] + output
        num //= 2

    return output


# str.slice() replacement
def slice(string: str, num: int) -> str:
    output: str = ""

    for i in range(num, len(string)):
        output += string[i]
    return output


# binary string equalizer
def is_lower(str1: str, str2: str, eq: bool) -> bool:
    if len(str1) > 0 and str1[0] == "0":
        return False
    elif len(str1) < len(str2):
        return True
    elif len(str1) > len(str2):
        return False
    return str1 <= str2 if eq else str1 < str2

# recursive function
# always splits string into val and rest max >= val >= min
# and merges it with substrings of rest with ","


def my_restore_sequence(digits: str, low: str, high: str) -> set[str]:
    next_char: int = 0
    current_str = ""
    if digits == "":
        return {""}

    output: set[str] = set()

    while is_lower(current_str, low, False):
        if next_char < len(digits):
            current_str += digits[next_char]
            next_char += 1
            continue
        return set()

    while is_lower(current_str, high, True):
        for string in my_restore_sequence(slice(digits, next_char), low, high):
            if len(string) > 0:
                output.add(current_str+","+string)
            else:
                output.add(current_str)
        if next_char < len(digits):
            current_str += digits[next_char]
            next_char += 1
            continue
        return output
    return output


def restore_sequence(digits: str, low: int, high: int) -> set[str]:

    convertor_arr: list[str] = ["0", "1"]

    return my_restore_sequence(digits, num_to_binstr(low, convertor_arr),
                               num_to_binstr(high, convertor_arr))


def main() -> None:
    assert restore_sequence("1111", 2, 3) == {"11,11"}
    assert restore_sequence("11110", 1, 6) == \
        {"1,1,1,10", "11,1,10", "11,110", "1,1,110", "1,11,10"}
    assert restore_sequence("1111", 100, 200) == set()
    assert restore_sequence("101010", 2, 10) \
        == {"10,10,10", "10,1010", "1010,10"}
    assert restore_sequence("1001", 1, 30) == {"1001", "100,1"}
    assert restore_sequence("111101111", 0b101, 0b111) == {"111,101,111"}
    assert restore_sequence("1110101", 1, 9) == {
        "1,1,10,101",
        "11,10,101",
        "11,10,10,1",
        "1,110,101",
        "1,110,10,1",
        "1,1,10,10,1",
    }


if __name__ == '__main__':
    main()
