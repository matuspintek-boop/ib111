def count_digit_in_sequence(digit, low, high):
    count = 0
    if low == 0 and digit == 0:
        count += 1
    for number in range(low, high + 1):
        while number > 0:
            if digit == number % 10:
                count += 1
            number = number // 10
    return count
