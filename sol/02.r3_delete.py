def delete_to_maximal(number):
    result = 0
    power = 1
    while number // power > 0:
        candidate = number // (power * 10) * power + number % power
        power *= 10
        if result < candidate:
            result = candidate
    return result


def delete_k_to_maximal(number, k):
    for i in range(k):
        number = delete_to_maximal(number)
    return number
