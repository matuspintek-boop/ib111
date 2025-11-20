def sum_divisors(number):
    result = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            result += i
    return result


def is_abundant(number):
    return sum_divisors(number) > number
