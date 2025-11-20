def sum_of_multiples(n):
    result = 0
    for i in range(n + 1):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    return result
