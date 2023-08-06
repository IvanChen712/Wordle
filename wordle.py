# wordle.py

import random
import contextlib
from string import ascii_letters, ascii_uppercase
from rich.console import Console
from rich.theme import Theme

console = Console(width=100, theme=Theme({'warning': 'red on yellow'}))

NUM_LETTERS = 5
NUM_GUESSES = 6
FILE = r'dewordle\wordle.txt'
letter_status_num = {letter: -1 for letter in ascii_uppercase}


# -1 unknown, 0 not exist, 1 exist but wrong pos, 2 exist and right pos


def main():
    guesses = ['_' * NUM_LETTERS] * NUM_GUESSES

    wordlist = get_wordlist(FILE)
    answer = get_answer(wordlist)

    with contextlib.suppress(KeyboardInterrupt):
        # when we forcibly interrupt, game over will appear before program ends
        for trial in range(1, NUM_GUESSES + 1):
            refresh_page(headline=f"Guess {trial}")
            show_guesses(guesses, answer)

            guesses[trial - 1] = guess_word(guesses, wordlist)

            if guesses[trial - 1] == answer:
                break

    game_over(trial, guesses, answer, answer in guesses)


def get_wordlist(file):
    f = open(file)
    wordlist = f.readlines()
    wordlist = [word.upper().strip() for word in wordlist]
    return wordlist


def get_answer(wordlist):
    answer = random.choice(wordlist)
    # print(answer)
    return answer


def guess_word(guesses, wordlist):
    guess = console.input('\n🤗 Guess word: ').upper()

    if any((invalid := letter) not in ascii_letters for letter in guess):
        console.print(f"Invalid letter: '{invalid}'.🤣👉🤡 Are you dreaming?🤔😃 ", style='warning')
        return guess_word(guesses, wordlist)

    if len(guess) != NUM_LETTERS:
        console.print(f"{guess} doesn't have 5 letters.😅🤔 So careless!😆🤗 ", style='warning')
        return guess_word(guesses, wordlist)

    if guess not in wordlist:
        console.print(f'{guess} is not in the wordlist.😅 Are you inventing a new word?🤭😀 ', style='warning')
        return guess_word(guesses, wordlist)

    if guess in guesses:
        console.print(f'You have already guessed {guess}.🤗 Your memory is impressive!😄😚 ', style='warning')
        return guess_word(guesses, wordlist)

    return guess


def refresh_page(headline):
    console.clear()
    console.rule(f"[bold blue]😍 {headline} 🤩[/]\n")


def count_letter(letter, word):  # count how many times a letter appears in a word
    times = 0
    for le in word:
        if le == letter:
            times += 1
    return times


def nth_certain_letter(index, word, letter):
    n = 0
    for i in range(index + 1):
        if letter == word[i]:
            n += 1
    return n


def prev_letter_index(index, word, letter):
    pre_index = 0
    for i in range(index):
        if letter == word[i]:
            pre_index = i
            break
    return pre_index


def show_guesses(guesses, answer):
    global letter_status_num
    letter_status = {letter: letter for letter in ascii_uppercase}

    for guess in guesses:
        styled_guess = []

        for index, (letter, correct) in enumerate(zip(guess, answer)):

            if letter == correct:
                style = 'bold white on green'
                letter_status_num[letter] = 2
                if nth_certain_letter(index, guess, letter) > count_letter(letter, answer):
                    styled_guess[prev_letter_index(index, guess, letter)] = f'[{"bold white on #666666"}]{letter}[/]'

            elif letter in answer:
                # handle exceptions, e.g., if we guess two 'c', but the answer only has one 'c'
                if nth_certain_letter(index, guess, letter) > count_letter(letter, answer):
                    style = 'bold white on #666666'
                else:
                    style = 'bold white on yellow'
                    letter_status_num[letter] = max(letter_status_num[letter], 1)

            elif letter in ascii_letters:
                style = 'bold white on #666666'
                letter_status_num[letter] = max(letter_status_num[letter], 0)

            else:
                style = 'dim'

            styled_guess.append(f'[{style}]{letter}[/]')

            if letter != "_":
                if letter_status_num[letter] == 2:
                    letter_status[letter] = f"[{'bold white on green'}]{letter}[/]"
                elif letter_status_num[letter] == 1:
                    letter_status[letter] = f"[{'bold white on yellow'}]{letter}[/]"
                elif letter_status_num[letter] == 0:
                    letter_status[letter] = f"[{'bold white on #666666'}]{letter}[/]"

        console.print(" ".join(styled_guess), justify="center")
    console.print("\n" + " ".join(letter_status.values()), justify="center")


def game_over(trial, guesses, answer, win):
    refresh_page(headline="Game Over")
    show_guesses(guesses, answer)
    if win:
        if trial == 1:
            console.print('WTF!😯 You must be cheating!😒🤥 ', style='warning')
        else:
            console.print(f'Congratulations!😎 You solve the wordle in {trial} steps.😁 ', style='warning')
    else:
        console.print(f'You lose.🤗🤔 The answer is {answer}.🤣👉🤡 Try again, please.😝 ', style='warning')


if __name__ == "__main__":
    main()
