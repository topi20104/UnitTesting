from unittest import mock
from unittest.main import main
import random

'''Made by Topi Aila'''


def RockPaperScissors(mockInput):
    #RPS list is for each different option on Rock Paper Scissors game.
    RPSList = ['rock','paper','scissors']
    
    userInput = input("rock, paper or scissors? \n").lower()
    if mockInput == '':
        RPSVar = random.choice(RPSList)
    else:
        RPSVar = mockInput
        
        
    if(RPSVar == 'rock'):
        print("The computer chose: rock")
    elif(RPSVar == 'paper'):
        print("The computer chose: paper")
    elif(RPSVar == 'paper'):
        print("The computer chose: scissors")


    #Rock > Scissors
    #Scissors > Paper
    #Paper > Rock

    winStatement = "Fail"
    #First we have if statement where the user always loses.
    if (RPSVar == 'rock' and userInput == 'scissors' or RPSVar == 'paper' and userInput == 'rock' or RPSVar == 'scissors' and userInput == 'paper'):
        print("you lose")
        winStatement = "Computer wins"
        return winStatement
    #Then all the cases where there is a draw.
    elif(RPSVar == 'rock' and userInput == 'rock' or RPSVar == 'paper' and userInput == 'paper' or RPSVar == 'scissors' and userInput == 'scissors'):
        print("it's a draw")
        winStatement = "Draw"
        return winStatement
    #Now all the other combinations are where the user wins
    elif(RPSVar == 'scissors' and userInput == 'rock' or RPSVar == 'rock' and userInput == 'paper' or RPSVar == 'paper' and userInput == 'scissors'):
        print("You win")
        winStatement = "User wins"
        return winStatement
    return winStatement