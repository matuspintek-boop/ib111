def coins(value):
    result = 0

    result += value // 5
    value %= 5

    result += value // 2
    value %= 2

    return result + value
