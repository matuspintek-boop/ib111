from ib111 import week_10  # noqa


# Napište (čistou) funkci, která dostane na vstupu množinu čísel a
# vrátí délku nejdelšího šestnáctkového kruhu, který se z nich dá
# vytvořit. Pokud se žádný kruh vytvořit nedá, vrátí 0.

# Šestnáctkový kruh je posloupnost čísel (bez opakování) taková, že
# každé další číslo začíná v šestnáctkovém zápisu stejnou cifrou,
# jakou končí číslo předchozí. Navíc první číslo v posloupnosti
# začíná stejnou číslicí, jakou končí poslední číslo.

first = int
last = int
num = int
Data = dict[first, list[tuple[last, num]]]


def get_first_last_dig(number: num) -> tuple[first, last, num]:
    number_copy = number
    last_d: last = number % 16
    first_d: first = -1
    while number > 0:
        first_d = number % 16
        number //= 16

    if first_d == -1:
        first_d = last_d
    return (first_d, last_d, number_copy)


# function returns bool (number already visited)
# and it's generation of visit, round of DFS graph ispection
def dfs_indexator(number: num, length: int,
                  data_set: set[tuple[num, int]]) -> tuple[bool, int]:
    output = False
    index = 0
    for i in range(length+1):
        if (number, i) in data_set:
            output = True
            index = i
    return (output, index)


# for each num in data we run dfs and
# write down all circles into record variable
def find_circle(already_visited: set[tuple[num, int]], current_length: int,
                current_num_first: int, data: Data, record: list[int]) -> None:

    for (last_digit, number) in data.get(current_num_first, []):

        num_in_set, gen = dfs_indexator(number,
                                        current_length, already_visited)

        if not num_in_set:
            find_circle(already_visited | {(number, current_length)},
                        current_length+1, last_digit, data, record)

        else:
            record.append(current_length - gen)


def maximum(list_: list[int]) -> int:
    max_val: int = 0
    for val in list_:
        max_val = max(val, max_val)

    return max_val


def hex_circle(numbers: set[int]) -> int:
    data: Data = {}
    for number in numbers:
        first_d, last_d, number = get_first_last_dig(number)
        if not data.get(first_d, False):
            data[first_d] = [(last_d, number)]
        else:
            data[first_d].append((last_d, number))

    record: list[int] = []

    for key in data.keys():
        find_circle(set(), 0, key, data, record)

    return maximum(record)


def main() -> None:
    assert hex_circle({0}) == 1
    assert hex_circle({16, 1}) == 1
    assert hex_circle(set()) == 0
    assert hex_circle({0xabc, 0x123}) == 0
    assert hex_circle({0xabcd, 0xdef, 0xfa}) == 3
    assert hex_circle({0xaba}) == 1
    assert hex_circle({0xabc, 0xca, 0xcd, 0xda}) == 3

    hexes = {0xabc, 0xca, 0xacd, 0xda}
    assert hex_circle(hexes) == 4
    assert hexes == {0xabc, 0xca, 0xacd, 0xda}


if __name__ == '__main__':
    main()
