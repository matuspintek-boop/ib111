import gzip


def autocorrect(dict_file: str, input_file: str,
                output_file: str) -> None:
    dictionary = read_dictionary(dict_file)

    with open(input_file) as file:
        text = file.read()
        word = ""

        with open(output_file, "w") as out:
            for char in text:
                if char.isalpha():
                    word += char
                else:
                    out.write(corrected_word(word, dictionary))
                    word = ""
                    out.write(char)
            out.write(corrected_word(word, dictionary))


def corrected_word(word: str,
                   dictionary: dict[int, set[str]]) -> str:
    words = dictionary.get(len(word), set())
    word = word.lower()
    if not words or word in words:
        return word
    return best_correction(word, words)


def read_dictionary(path: str) -> dict[int, set[str]]:
    res: dict[int, set[str]] = {}
    with gzip.open(path, 'rt') as data:
        for word in data:
            word = word.strip()
            key = len(word)
            if key not in res:
                res[key] = set()
            res[key].add(word)
    return res


def best_correction(word: str, matches: set[str]) -> str:
    candidates = closest_by_hamming(word, matches)
    return min(closest_by_ends(word, candidates))
