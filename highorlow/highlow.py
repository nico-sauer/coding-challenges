#Higher or Lower Number Game - www.101computing.net/higher-or-lower-number-game/
from random import randint

#numberToGuess = randint(1,100)
numberToGuess = randint(1,100)
userGuess = int(input("Guess a number between 1 and 100 until you get it right: "))

#Complete the code here...

while numberToGuess != userGuess: 
    
    if numberToGuess > userGuess:
        nextGuess = int(input("Higher!\n>"))
        userGuess = nextGuess
    else:
        nextGuess = int(input("Lower!\n>"))
        userGuess = nextGuess
print("You win.")
