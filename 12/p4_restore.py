from ib111 import week_12  # noqa


# Napište čistou funkci ‹restore_sequence›, která dostane neprázdný řetězec
# složený pouze z číslic 0 a 1 a vrátí množinu všech možných
# řetězců, které vzniknou doplněním znaků čárky ‹','› do původního
# řetězce tak, aby části jimi oddělené byly dvojkové zápisy čísel
# v intervalu od ‹low› do ‹high› včetně. Hodnota ‹low› bude vždy
# alespoň 1. Rozdělení musí být takové, že žádný zápis neobsahuje
# levostranné nuly.

# zacinam od zaciatku stringu, navolim si hodnoty od low az po hight, zvysok strigu odseknem 
# a znovu zavolam rovnaku funkciu ktora mi vrati mnozinu moznych stringov

def slice(string: str, num: int) -> str:
    output: str = ""

    for i in range(num, len(string)):
        output += string[i]
    return output

def my_restore_sequence(digits: str, low: str, high: str) -> set[str]:
    print(digits)
    next_char: int = 0
    current_str = ""
    if digits == "":
        return {""}

    output: set[str] = set()

    while current_str < low:
        if next_char < len(digits):
            current_str += digits[next_char]
            next_char += 1
            continue
        return set()
    

    while current_str <= high:
        print(slice(digits, next_char), digits, next_char, my_restore_sequence(slice(digits, next_char), low, high))
        for string in my_restore_sequence(slice(digits, next_char), low, high):
            output.add(current_str+","+string)
        if next_char < len(digits):
            current_str += digits[next_char]
            next_char += 1
            continue
        return output
    
print(my_restore_sequence("1111", "10", "11"))

def restore_sequence(digits: str, low: int, high: int) -> set[str]:
    otput: set[str] = set()
    pass


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
