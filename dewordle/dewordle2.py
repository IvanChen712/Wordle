# Example input: 
# crane 00012
# 0: not exist
# 1: exist, but wrong position
# 2: exist, and right position

letters_1 = set()
letters_2 = set()
correct_word = {i: set(chr(j) for j in range(ord('a'), ord('z') + 1)) for i in range(5)}


def remove_letter(letter, correct_word):
    for letter_set in correct_word.values():
        letter_set.discard(letter)
    return


f = open("wordle.txt")
words = f.readlines()
words = [word.strip() for word in words]  # remove '\n'

print(f'Input your guesses word and corresponding results.')
print(f'The word should have five letters and the results should have five numbers. ')
trial = 1

while True:

    # input
    user_input = input(f'Attempt {trial}:').strip()
    if ' ' in user_input:
        input_word, results = user_input.split()
        results = [int(r) for r in results]
        input_word = input_word.lower()
    else:
        print('Invalid input. Please enter a space-separated word and results.')
        continue

    if len(input_word) != 5:
        print('Invalid input. Please input a word with five letters.')
        continue

    if len(results) != 5:
        print('Invalid input. Please input the results with five numbers.')
        continue

    if not all(result in {0, 1, 2} for result in results):
        print('Invalid input. Please use only 0, 1, or 2 for the results.')
        continue

    if not input_word.isalpha():
        print('Invalid input. Please input a word containing only letters.')
        continue

    if all(result == 2 for result in results):
        print(f'Congratulations! You solved the wordle in {trial} steps.\n')
        break

    if input_word not in words:
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
            continue

    # process input information
    for i in range(0, 5):
        if results[i] == 0:  # letter does not exist
            if input_word[i] in letters_1 or input_word[i] in letters_2:
                correct_word[i].discard(input_word[i])
            else:
                remove_letter(input_word[i], correct_word)

        elif results[i] == 1:  # letter exists, but pos wrong
            letters_1.add(input_word[i])
            correct_word[i].discard(input_word[i])

        else:  # letter exists and correct pos
            letters_2.add(input_word[i])
            correct_word[i] = set(input_word[i])

    # find remaining words
    remaining_words = set()
    for word in words:
        if all(word[i] in correct_word[i] for i in range(5)) and letters_1.issubset(set(word)):
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
