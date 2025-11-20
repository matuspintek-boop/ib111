def powers(n, k):
    result = 0
    for i in range(n):
        result += (i + 1) ** k
    return result
