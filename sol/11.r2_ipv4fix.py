def split(orig: str, index: int) -> tuple[str, str]:
    left = right = ''
    for i in range(index):
        left += orig[i]
    for i in range(index, len(orig)):
        right += orig[i]
    return left, right


def decode_decimal(digits: str) -> int:
    result = 0
    table = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
             "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}

    for digit in digits:
        result *= 10
        result += table[digit]

    return result


def ipv4_restore_rec(digits: str, count: int, current: list[str],
                     result: set[str]) -> set[str]:
    if count == 0:
        if digits == "":
            result.add(".".join(current))
        return result

    for i in range(1, len(digits) + 1):
        left, right = split(digits, i)
        if decode_decimal(left) >= 256:
            break
        current.append(left)
        ipv4_restore_rec(right, count - 1, current, result)
        current.pop()

    return result


def ipv4_restore(digits: str) -> set[str]:
    return ipv4_restore_rec(digits, 4, [], set())
