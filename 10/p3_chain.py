from ib111 import week_10  # noqa


# Napište predikát, který dostane na vstupu množinu čísel ⟦M⟧ a
# délku ⟦n⟧ a rozhodne, existuje-li navazující posloupnost čísel
# délky právě ⟦n⟧. Navazující posloupnost je taková, kde každé další
# číslo začíná v jedenáctkovém zápisu stejnou číslicí, jakou končí
# předchozí. Čísla se v posloupnosti nesmí opakovat.

first = int
last = int
Num = int
Data = dict[first, list[tuple[last, Num]]]


def convert_to_eleven_base(num: int) -> tuple[first, last]:
    last_digit: int = num % 11
    first_digit: int = -1
    while num > 0:
        first_digit = num % 11
        num //= 11

    if first_digit == -1:
        first_digit = last_digit

    return (first_digit, last_digit)


def find_all_connections(start: int, already_seeen: set[int],
                         current_count: int, goal: int, data: Data) -> bool:
    if current_count == goal:
        return True

    for (connection, num) in data.get(start, []):
        if num not in already_seeen:
            if find_all_connections(connection, already_seeen | {num},
                                    current_count+1, goal, data):
                return True
    return False


def elven_chain(numbers: set[int], length: int) -> bool:
    data: Data = {}
    for num in numbers:
        first_digit, last_digit = convert_to_eleven_base(num)
        new_list: list[tuple[last, Num]] = []
        last_digits = data.get(first_digit, new_list)
        last_digits.append((last_digit, num))
        data[first_digit] = last_digits

    if length == 0:
        return True

    for key in data.keys():
        if find_all_connections(key, set(), 0, length, data):
            return True
    return False


def main() -> None:
    assert elven_chain({0}, 1)
    assert elven_chain({57, 25, 36}, 3)
    assert elven_chain(set(), 0)
    assert elven_chain({1}, 1)
    assert elven_chain({146, 12}, 2)
    assert elven_chain({146, 23}, 2)
    assert not elven_chain({146, 11}, 2)
    assert not elven_chain({146, 13}, 2)
    assert not elven_chain({2, 13}, 3)

    numbers = {146, 12}
    assert elven_chain(numbers, 2)
    assert numbers == {146, 12}


if __name__ == '__main__':
    main()
