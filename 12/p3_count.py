from ib111 import week_12  # noqa


# Napište funkci ‹count_seq›, která nad desítkovou reprezentací
# nezáporného celého čísla ‹num› provede následující výpočet:

#  1. vybere všechny cifry, po kterých následuje alespoň ‹seq›
#     stejných cifer; pro účely této kontroly chápeme ‹num›
#     cyklicky, tzn. po poslední cifře následuje opět první,
#  2. vybrané cifry sečte a součet vrátí.

# Cykličnost v bodě 1 můžeme chápat jako nekonečné opakování ‹num›,
# např. v čísle 123 následují po cifře 2 cifry 3, 1, 2, 3, 1, atd.

# Příklady výpočtu:

#  • pro ‹num=111222› a ‹seq=2› je výsledkem 3 (1 + 2), protože po
#    první (1) a čtvrté (2) cifře následují 2 stejné cifry,
#  • pro ‹num=1111› a ‹seq=1› je výsledkem 4, protože po každé cifře
#    následuje alespoň jedna stejná cifra,
#  • pro ‹num=1234› a ‹seq=0› je výsledkem součet všech číslic,
#    totiž 10.
def decompose(num: int) -> list[int]:
    output: list[int] = []

    while num > 0:
        output.append(num % 10)
        num //= 10

    output.reverse()

    return output


def count_seq(num: int, seq: int) -> int:

    output_sum: int = 0
    work_l: list[int] = decompose(num)
    lenght: int = len(work_l)

    for index, val in enumerate(work_l):
        i: int = 1
        sequence: bool = True
        while i <= seq and sequence:
            sequence = work_l[(index + i) % lenght] == val
            i += 1
        if sequence:
            output_sum += val

    return output_sum


def main() -> None:
    assert count_seq(1122, 1) == 3
    assert count_seq(111222, 2) == 3
    assert count_seq(1111, 1) == 4
    assert count_seq(1111, 3) == 4
    assert count_seq(1111, 20) == 4
    assert count_seq(1234, 1) == 0
    assert count_seq(41214, 1) == 4
    assert count_seq(1234, 0) == 10
    assert count_seq(412213334, 1) == 12
    assert count_seq(110002331, 2) == 1
    assert count_seq(222220, 4) == 2
    assert count_seq(222022, 3) == 4
    assert count_seq(41214, 0) == 12
    assert count_seq(818275977931166178424892653779931348, 1) == 38
    assert count_seq(882227597793116661784248926663779931348, 2) == 22
    assert count_seq(818275977931166178424892653779931348, 0) == 190


if __name__ == "__main__":
    main()
