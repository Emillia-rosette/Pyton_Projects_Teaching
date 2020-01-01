# Guess The Number game

import random

# welcome the user

fname = input(" Hi, What is your name ?")
print("Hello!", fname)

# call random function from random module
numRandom = random.randint(0, 20)
guessLimit = random.randint(0,10)

numCount = 0
guessFound = 9

while numCount < 10:
    userChoice = int(input("Please, guess a number between 1 to 30: "))

    if userChoice == guessFound:
        print("Well done! You have found the number")
        break
    elif userChoice > numRandom:
        numCount = numCount + 1
        guessLimit = guessLimit -1
        print("Your number is too high, You have", guessLimit, "counts left")
    elif userChoice < numRandom:
        numCount = numCount + 1
        guessLimit = guessLimit - 1
        print("Your number is too low, You have", guessLimit, "counts left")
    else:
        print("Wrong entry, Please try again!")
if guessLimit == 0:
    print("Ops! You have run out of chances. Try again next time")