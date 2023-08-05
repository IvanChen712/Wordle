# wordle.py

import random
import contextlib
from string import ascii_letters, ascii_uppercase
from rich.console import Console
from rich.theme import Theme

console = Console(width=100, theme=Theme({'warning': 'red on yellow'}))

NUM_LETTERS = 5
NUM_GUESSES = 6
FILE = 'dewordle\wordle.txt'


def main():
    guesses = ['_' * NUM_LETTERS] * NUM_GUESSES
    wordlist = get_wordlist(FILE)
    answer = get_answer(wordlist)

    with contextlib.suppress(KeyboardInterrupt):
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


def show_guesses(guesses, answer):
    letter_status = {letter: letter for letter in ascii_uppercase}
    for guess in guesses:
        styled_guess = []
        for letter, correct in zip(guess, answer):
            if letter == correct:
                style = 'bold white on green'
            elif letter in answer:
                style = 'bold white on yellow'
            elif letter in ascii_letters:
                style = 'bold white on #666666'
            else:
                style = 'dim'

            styled_guess.append(f'[{style}]{letter}[/]')

            if letter != "_":
                letter_status[letter] = f"[{style}]{letter}[/]"

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
