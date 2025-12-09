from ib111 import week_12  # noqa
from math import isqrt


# Napište čistou funkci ‹highly_composite›, která dostane na vstupu
# množinu přirozených čísel a vrátí množinu těch z nich, která jsou
# vysoce složená relativně k původní množině. Přirozené číslo je
# vysoce složené, má-li striktně víc dělitelů (a to včetně těch,
# které v zadané množině nejsou), než libovolné menší číslo ze
# zadané množiny.

def count_divisors(num: int) -> int:
    divisors: set[int] = set()
    divisor: int = 1

    upper_border: int = isqrt(num)

    while divisor <= upper_border:
        if num % divisor == 0:
            divisors.add(divisor)
            divisors.add(num // divisor)
        divisor += 1

    return len(divisors)

def highly_composite(numbers: set[int]) -> set[int]:
    work_list: list[int] = list(numbers)
    work_list.sort()
    print(work_list)
    
    output: set[int] = set()
    output.add(work_list[0])
    ancestor = work_list[0]
    counted_divisors  = False

    for num in work_list:
        if num % ancestor == 0:
            ancestor = num
            output.add(num)
            counted_divisors = False
        else:
            current_divisors = count_divisors(num)
            if counted_divisors:
                if current_divisors > ancestor_divisors:
                    ancestor_divisors = current_divisors
                    ancestor = num
                    output.add(num)
                    counted_divisors = True
            else:
                ancestor_divisors = count_divisors(ancestor)
                if current_divisors > ancestor_divisors:
                    ancestor_divisors = current_divisors
                    ancestor = num
                    output.add(num)
                    counted_divisors = True

                            

    return output


def main() -> None:
    small_c = {1, 2, 4, 6, 12, 24, 36, 48}

    assert highly_composite({1, 3, 7, 12}) == {1, 3, 12}
    assert highly_composite(set(range(1, 50))) == small_c

    big1 = set(range(1, 100)) | big_set(6, 4)
    big2 = set(range(1, 1000)) | big_set(6, 8)
    big1_c = {60, big_n(4, 2), big_n(5, 2), big_n(4, 3), big_n(5, 3)}
    big2_c = {60, 120, 180, 240, 360, 720, 840,
              big_n(5, 5), big_n(5, 6), big_n(5, 7)}
    assert highly_composite(big1) == small_c | big1_c
    assert highly_composite(big2) == small_c | big2_c


def big_set(a: int, b: int) -> set[int]:
    return set([big_n(i, j)
                for i in range(1, a)
                for j in range(b)])


def big_n(i: int, j: int) -> int:
    num: int = 7 ** i * 10099 ** j
    return num


if __name__ == '__main__':
    main()
