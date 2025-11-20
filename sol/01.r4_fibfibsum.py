def fibfibsum(count):
    result = 0

    index_a = 1
    index_b = 1

    a = 1
    b = 1
    i = 1

    for _ in range(count):
        while i < index_a:
            c = a + b
            a = b
            b = c
            i += 1
        result += a

        index_c = index_a + index_b
        index_a = index_b
        index_b = index_c
    return result
