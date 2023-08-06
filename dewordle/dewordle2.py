# Example input: 
# crane 00012
# 0: not exist
# 1: exist, but wrong position
# 2: exist, and right position

letters_1 = []
letters_2 = []
correct_word = {i: set(chr(j) for j in range(ord('a'), ord('z') + 1)) for i in range(5)}


def remove_letter(letter, correct_w):
    for letter_set in correct_w.values():
        letter_set.discard(letter)
    return


def list_minus(l1, l2):
    result = [x for x in l1 if x not in l2 or l1.count(x) > l2.count(x)]
    return result


def list_contain(l1, l2):
    if all(x in l2 and l1.count(x) <= l2.count(x) for x in l1):
        return True


def letter_num(letter, in_word, results, result):
    times = 0
    for i in range(5):
        if in_word[i] == letter and results[i] == result:
            times += 1
    return times


def get_words(file):
    f = open(file)
    wordlist = f.readlines()
    wordlist = [w.strip() for w in wordlist]  # remove '\n'
    return wordlist


def get_input(wordlist):
    user_input = input(f'Attempt {trial}:').strip()
    if ' ' in user_input:
        in_word, results = user_input.split()
        results = [int(r) for r in results]
        in_word = in_word.lower()
    else:
        print('Invalid input. Please enter a space-separated word and results.')
        return get_input(wordlist)

    if len(in_word) != 5:
        print('Invalid input. Please input a word with five letters.')
        return get_input(wordlist)

    if len(results) != 5:
        print('Invalid input. Please input the results with five numbers.')
        return get_input(wordlist)

    if not all(result in {0, 1, 2} for result in results):
        print('Invalid input. Please use only 0, 1, or 2 for the results.')
        return get_input(wordlist)

    if not in_word.isalpha():
        print('Invalid input. Please input a word containing only letters.')
        return get_input(wordlist)

    if in_word not in wordlist:
        print('Your input word is not in the possible list of words. Are you sure you have entered this word? [y/n]')
        while True:
            cmd = input()
            if cmd == 'y':
                print('OK. Let\'s continue.\n')
                flag = False
                break
            elif cmd == 'n':
                print('Please input again.\n')
                flag = True
                break
            else:
                print('You should enter y/n. [y/n]')
        if flag:
            return get_input(wordlist)

    return in_word, results


words = get_words("wordle.txt")

print(f'Input your guesses word and corresponding results.')
print(f'The word should have five letters and the results should have five numbers. ')
trial = 1

while True:

    input_word, input_results = get_input(words)

    if all(result == 2 for result in input_results):
        print(f'Congratulations! You solved the wordle in {trial} steps.\n')
        break

    # process input information
    for i in range(0, 5):
        if input_results[i] == 0:  # letter does not exist
            if input_word[i] in letters_1 or input_word[i] in letters_2:
                correct_word[i].discard(input_word[i])
            else:
                remove_letter(input_word[i], correct_word)
        elif input_results[i] == 1:  # letter exists, but pos wrong
            if (input_word[i] not in letters_1 or letter_num(input_word[i], input_word, input_results, 1) +
                    letter_num(input_word[i], input_word, input_results, 2) > letters_1.count(input_word[i])):
                letters_1.append(input_word[i])
            correct_word[i].discard(input_word[i])

        else:  # letter exists and correct pos
            if (input_word[i] not in letters_2 or
                    letter_num(input_word[i], input_word, input_results, 2) > letters_2.count(input_word[i])):
                letters_2.append(input_word[i])
            if input_word[i] in letters_1:
                letters_1.remove(input_word[i])
            correct_word[i] = set(input_word[i])

    # find remaining words
    remaining_words = set()
    for word in words:
        if all(word[i] in correct_word[i] for i in range(5)) and list_contain(letters_1, list_minus(word, letters_2)):
            remaining_words.add(word)

    # print number and words
    words = remaining_words
    if len(words) < 500:
        count = 0
        for word in words:
            print(word, end="  ")
            count += 1
            if count % 12 == 0:
                print()

    if len(words) == 1:
        print(f'\nOnly one word left.\n')
    elif len(words) == 0:
        print(f'\nIt seems that there is something wrong with your given inputs. PLease input again.\n')
        break
    else:
        print(f'\n{len(words)} words left in total.\n')

    trial += 1
