from math import acos, sqrt, pi


def recognize_language(lang_data: dict[str, dict[str, int]],
                       text_file: str) -> str:
    lang_freqs = lang_vectors(lang_data)
    file_freq = letter_freq_vector(text_file)

    min_angle = pi
    min_lang = ''

    for lang, lang_freq in lang_freqs.items():
        a = vector_angle(file_freq, lang_freq)
        if a < min_angle:
            min_angle = a
            min_lang = lang

    return min_lang


def letter_freq_vector(filename: str) -> list[int]:
    freqs = [0 for i in range(26)]
    indices = enumerate(list("abcdefghijklmnopqrstuvwxyz"))
    letters = dict([(letter, idx) for idx, letter in indices])

    with open(filename) as file:
        text = file.read()

        for char in text:
            if "a" <= char <= "z" or "A" <= char <= "Z":
                freqs[letters[char.lower()]] += 1

    return freqs


def lang_vectors(languages: dict[str, dict[str, int]]) \
        -> dict[str, list[int]]:
    res: dict[str, list[int]] = {}
    for language, freqs in languages.items():
        res[language] = [y for x, y in freqs.items()]

    return res


def vector_angle(v1: list[int], v2: list[int]) -> float:
    assert len(v1) == len(v2)

    dot_product = sum([v1[i] * v2[i] for i in range(len(v1))])
    len_v1 = sqrt(sum([x ** 2 for x in v1]))
    len_v2 = sqrt(sum([x ** 2 for x in v2]))
    return acos(dot_product / (len_v1 * len_v2))
