letter_freq = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
letter_freq_pos = {chr(i): [0, 0, 0, 0, 0] for i in range(ord('a'), ord('z') + 1)}

f = open("wordle.txt")
words = f.readlines()
words = [word.strip() for word in words] # remove '\n'

for word in words:
    for i, letter in enumerate(word):
        letter_freq[letter] += 1
        letter_freq_pos[letter][i] += 1

# print(letter_freq)
for key, values in letter_freq_pos.items():
    print(f'{key}: {letter_freq_pos[key]}')
