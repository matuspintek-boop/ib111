def reverse(number):
    result = 0
    while number > 0:
        digit = number % 10
        result = result * 10 + digit
        number = number // 10
    return result


def is_palindrome(number):
    return number == reverse(number)
