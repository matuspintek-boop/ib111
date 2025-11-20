

def add_char_to_words(words: set[str], char: str) -> set[str]:
    result = set()
    for word in words:
        result.add(char + word)
    return result


def weighted_words(length: nat, weight: nat) -> set[str]:
    if weight == 0 and length == 0:
        return {""}

    if weight > length or length == 0:
        return set()

    to_add_zero = weighted_words(length - 1, weight)
    to_add_nonzero = weighted_words(length - 1, weight - 1)
    result = add_char_to_words(to_add_zero, "0")
    result.update(add_char_to_words(to_add_nonzero, "1"))
    result.update(add_char_to_words(to_add_nonzero, "2"))

    return result
