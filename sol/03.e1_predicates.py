def all_greater_than(sequence, n):
    for x in sequence:
        if x <= n:
            return False
    return True


def any_even(sequence):
    for x in sequence:
        if x % 2 == 0:
            return True
    return False
