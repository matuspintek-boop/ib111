def is_prime(number):
    if number < 2:
        return False
    divisor = 2
    while divisor ** 2 <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True
