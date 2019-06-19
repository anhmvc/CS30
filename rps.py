'''
Description: A program that implements multiple versions of the classic game Rock Paper Scissors, with a person playing against the computer.
(I got stuck with some syntax errors in my code initially, and I used Google and StackOverflow for help debugging it. I did not discuss this 
assignment with any classmates.)
Written By: Anh Mac
Date: 10/10/2018
'''
# the choice function is needed in the last problem below
from random import choice

pChoice = input("Please enter player's move of 'rock', 'paper', or 'scissors'? ").lower()
cChoice = input("Please enter computer's move of 'rock', 'paper', or 'scissors? ").lower()

# a version of rock-paper-scissors where the computer cheats
# and always wins.
# pChoice is the person's choice of a move: either 'rock', 'paper', or 'scissors'.
# returns either 'person wins', 'computer wins', or 'tie game'.
def rpsCheat(pChoice):
    return "Computer wins!"

print("rpsCheat implements a version of rock-paper-scissors where the computer cheats and always wins.")
print(rpsCheat(pChoice))

# a version of rock-paper-scissors where the computer
# always chooses rock.
# pChoice is the person's choice of a move: either 'rock', 'paper', or 'scissors'.
# returns either 'person wins', 'computer wins', or 'tie game'.
def rpsRock(pChoice):
    if pChoice == 'rock':
        return "Tie game!"
    elif pChoice == 'paper':
        return "Person wins!"
    else:
        return "Computer wins!"

print("rpsRock implements a version of rock-paper-scissors where the computer always chooses rock.")
print(rpsRock(pChoice))

# an implementation of rock-paper-scissors for two players.
# pChoice is the person's choice of a move: either 'rock', 'paper', or 'scissors'.
# cChoice is the computer's choice of a move, with the same three possible values.
# returns either 'person wins', 'computer wins', or 'tie game'.
def rps2(pChoice, cChoice):
    if pChoice == cChoice:
        return "Tie game!"
    elif pChoice == 'rock' and cChoice == 'scissors':
        return "Person wins!"
    elif pChoice == 'paper' and cChoice == 'rock':
        return "Person wins!"
    elif pChoice == 'scissors' and cChoice == 'paper':
        return "Person wins!"
    else:
        return "Computer wins!"

print("rps2 implements a version of rock-paper-scissors for two players.")
print(rps2(pChoice, cChoice))

# an implementation of rock-paper-scissors where the computer
# chooses its move randomly.
# pChoice is the person's choice of a move: either 'rock', 'paper', or 'scissors'.
# returns either 'person wins', 'computer wins', or 'tie game'.
def rpsRandom(pChoice):
    return rps2(pChoice, choice(['rock', 'paper', 'scissors']))

print("rpsRandom implements a version of rock-paper-scissors where the computer chooses its move randomly.")
print(rpsRandom(pChoice))
