def most_common(path: str) -> list[str]:

    with open(path) as file:
        all_words = file.read().split()

        word_freq: dict[str, int] = {}
        for word in all_words:
            word = "".join([char for char in word if char.isalpha()])
            word = word.lower()
            word_freq[word] = word_freq.get(word, 0) + 1

        items = [(-freq, word) for word, freq in word_freq.items()]
        result = []
        for i, (_, word) in enumerate(sorted(items)):
            if i == 3:
                break
            result.append(word)
        return result
