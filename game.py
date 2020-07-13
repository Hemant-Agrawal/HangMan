import random


def replace(letter, count):
    last = -1
    for _ in range(count):
        last = word.find(letter, last+1)
        hint[last] = letter


def error_check(letter):
    if len(letter) != 1:
        print("You should input a single letter")
        return False
    elif letter.lower() == letter and letter.isalpha():
        return True
    print("It is not an ASCII lowercase letter")
    return False       
    

print("H A N G M A N ")
while True:
    choice = input('Type "play" to play the game, "exit" to quit: ')
    if choice != 'play':
        break
    wordlist = ['python', 'java', 'kotlin', 'javascript']
    word = random.choice(wordlist)
    hint = ['-'] * len(word)
    lives = 8
    typed = []
    while lives > 0:
        print('\n', ''.join(hint))
        guess = input("Input a letter: ")
        if error_check(guess):
            if guess not in typed:
                typed.append(guess)
            else:
                print("You already typed this letter")
                continue
            if guess not in word:
                print("No such letter in the word")
                lives -= 1
            else:
                replace(guess, word.count(guess))
        if ''.join(hint) == word:
            print("You guessed the word",word+"!")
            print("You survived!")
            break
    else:
        print("You are hanged!")
