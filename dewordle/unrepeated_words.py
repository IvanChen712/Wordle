from wordle import get_wordlist


def has_unique_letters(word):
    return len(set(word)) == len(word)


def has_unique_letters_words(*words):
    combined_letters = "".join(words)
    return len(set(combined_letters)) == len(combined_letters)


def find_unique_combinations(words, combination_length, letters_needed_count):
    def backtrack(start, path):
        if len(path) == combination_length:
            combined_letters = "".join(path)
            if len(set(combined_letters)) == letters_needed_count:
                unique_combinations.append(tuple(path))
            return

        for i in range(start, len(words)):
            if has_unique_letters(words[i]):
                backtrack(i + 1, path + [words[i]])

    unique_combinations = []
    backtrack(0, [])

    return unique_combinations


if __name__ == "__main__":
    wordle_wordlist = get_wordlist("test.txt")
    unique_words = [word for word in wordle_wordlist if has_unique_letters(word)]
    unique_five_words_set = find_unique_combinations(unique_words, 5, 25)

    for five_words in unique_five_words_set:
        print(five_words)
