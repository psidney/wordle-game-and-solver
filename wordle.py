from colorama import init, Fore, Back, Style
import random

init()

words = []
with open('5letter.txt') as f:
    line = f.readline().replace('\n','')
    while line:
        words.append(line)
        line = f.readline().replace('\n','')

correctWord = random.choice(words)

winFlag = False

turns = []

def drawGuesses(turns):
    print(Style.RESET_ALL)
    i = 1
    for turn in turns:
        stringToPrint = f'{i}.) '
        for c in turn:
            stringToPrint += c
        stringToPrint += Style.RESET_ALL
        print(stringToPrint)
        i+=1

correctWordLetters = [char for char in correctWord]

while winFlag == False:
    drawGuesses(turns)
    guess = input("...?").lower()
    if guess == correctWord:
        winFlag = True
    elif guess not in words:
        print('Not a valid word!')
    else:
        guessLetters = [char for char in guess]
        i = 0
        checkList = []
        while i<5:
            if guessLetters[i] == correctWordLetters[i]:
                checkList.append(Back.GREEN + Fore.BLACK + guessLetters[i])
            elif guessLetters[i] in correctWordLetters:
                checkList.append(Back.YELLOW + Fore.BLACK + guessLetters[i])
            else:
                checkList.append(Back.RED + Fore.BLACK + guessLetters[i])
            i+=1

        turns.append(checkList)
        if len(turns)==6:
            print(f'YOU LOSE. Correct word: {correctWord}')
            exit()
print('You win!')