f = open("wordle.txt")
words = f.readlines()

while True:
    cmd = input()
    if cmd[0] not in "+-" or not cmd[1:].isalpha():
        print('Invalid input')
        continue

    if cmd[0] == "+":
        for ch in cmd[1:]:
            words = set(filter(lambda word: ch in word, words))
    
    elif cmd[0] == "-":
        for ch in cmd[1:]:
            words = set(filter(lambda word: not ch in word, words))
    
    if len(words) < 100:
        count = 0
        for word in words:
            word = word.strip()
            print(word, end="  ")
            count += 1
            if count % 12 == 0:
                print()
    
    print(f'\n{len(words)} words left in total.\n' )
