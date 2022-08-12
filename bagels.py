import random
import time
import numpy

fermi = 'One digit is correct but in wrong position'
pico = 'One digit is correct and in right position'
bagels = 'No digit is correct'


def getsecretnum():
    secret_num = random.randrange(100, 999)
    return secret_num


def getclues(guess, secretNum):
    clues = []
    for i in guess:
        if guess[i] == secretNum[i]:
            clues.append('Pico')
        elif i in secretNum:
            clues.append('Fermi')
    if len(clues) == 0:
        return 'Bagels'
    else:
        return sorted(clues)




def main(secret_num):
    print('''Welcome to the game, you have 8 guesses to guess a 3 digit number
    I'll give you hints on the way''')
    time.sleep(5)

    guess = input("Type your guess: ")
    guesscount = 0
    while guesscount < 8:
        for i in range(8):
            if secret_num == guess:
                print('You won :))))')
                break
