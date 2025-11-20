# unconfuse ib111.py
from p5_credit import is_valid_card, check_digit


def digits(number):
    counter = 0
    while number >= 10 ** counter:
        counter += 1
    return counter


def first_n_digits(number, n):
    return number // (10 ** (digits(number) - n))


def is_visa(number):
    if not is_valid_card(number):
        return False
    digs = digits(number)
    if digs == 13 or digs == 16 or digs == 19:
        return first_n_digits(number, 1) == 4
    return False


def is_mastercard(number):
    if not is_valid_card(number) or digits(number) != 16:
        return False

    if 50 <= first_n_digits(number, 2) <= 55:
        return True

    if 22100 <= first_n_digits(number, 5) <= 27209:
        return True

    return False
