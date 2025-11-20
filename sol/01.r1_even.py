def even(n):
    result = 0
    for i in range(n):
        number = 2 * (i + 1)
        result += number ** 2
    return result
