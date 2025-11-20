def divisors(number):
    count = 1  # number always divides itself
    divisor = 1
    maximal = number // 2
    while divisor <= maximal:
        if number % divisor == 0:
            count += 1
        divisor += 1
    return count
