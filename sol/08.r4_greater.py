def get_digit(num: int, power: int, base: int) -> int:
    return (num // base ** power) % base


def next_greater(num: int) -> int | None:
    base = 10
    swap_digit = 0
    swap_power = 0
    min_power = 0
    min_digit = base
    last = 0

    while base ** swap_power <= num:
        swap_digit = get_digit(num, swap_power, base)
        if swap_digit < last:
            break
        swap_power += 1
        last = swap_digit

    if base ** swap_power > num:
        return None

    for i in range(swap_power - 1, -1, -1):
        digit = get_digit(num, i, base)
        if digit < min_digit and digit > swap_digit:
            min_power = i
            min_digit = digit

    num += (min_digit - swap_digit) * base ** swap_power
    num += (swap_digit - min_digit) * base ** min_power

    low_order = [get_digit(num, i, base)
                 for i in range(0, min_power + 1)]

    num //= base ** (min_power + 1)
    for digit in sorted(low_order):
        num *= base
        num += digit

    return num
