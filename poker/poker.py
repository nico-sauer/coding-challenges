#Poker Dice Challenge - www.101computing.net/fancy-a-game-of-poker-dice/
import random

die1=random.randint(1,6)
die2=random.randint(1,6)
die3=random.randint(1,6)
print("First Roll:{}\nSecond Roll:{}\nThird Roll:{}".format (die1, die2, die3))

if die1 == die2 and die2 == die3:
    print("Three of a kind!!!")
elif die1 == die2 or die2 == die3 or die1 == die3:
    print("1 Pair!!")
else:
    print("Better luck next time.")