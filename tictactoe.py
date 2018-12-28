import subprocess as sp
from printGrid import *
from random import randint
from change_grid_x import changeGridX
from change_grid_o import changeGridO
from sys import exit
from os import system

grid = [ [" "," "," ","#"," "," "," ","#"," "," "," "], [" "," "," ","#"," "," "," ","#"," "," "," "],[" "," "," ","#"," "," "," ","#"," "," "," "], ["#","#","#","#","#","#","#","#","#","#","# "], [" "," "," ","#"," "," "," ","#"," "," "," "],[" "," "," ","#"," "," "," ","#"," "," "," "], [" "," "," ","#"," "," "," ","#"," "," "," "],["#","#","#","#","#","#","#","#","#","#","# "],[" "," "," ","#"," "," "," ","#"," "," "," "],[" "," "," ","#"," "," "," ","#"," "," "," "],[" "," "," ","#"," "," "," ","#"," "," "," "]]
gridLocal = grid

def clear(): sp.call('clear',shell=True)

clear()
playerTurns = []
computerTurns = [] 

def startGame():
    
    print("This is a game of TicTacToe:")
    print('''The controls are as such:
    For each turn, chose between 1 to 9 which will correspond to position of your mark
    Like follows:
    1   2   3
    4   5   6
    7   8   9
    
    
    ''')
    printGrid(gridLocal)
    checkCorrectInput()

def checkCorrectInput():
    if(checkDraw() == False):
        print("Player's Turn:")
        print("Choose a position (1 --> 9)")        
        x = input()
        if(x.isdigit() == True):
            x = int(x)
            if(x in computerTurns):
                print("Computer has already played this")
                checkCorrectInput()
            
            elif(x in playerTurns):
                print("Player has already played this")
                checkCorrectInput()
                
            else:
                if((x >= 1) and (x <= 9)):
                    playerTurn(x)
                else:
                    print("Please enter a number between 1 and 9")
                    checkCorrectInput()
        else:
            print("Please enter a number between 1 and 9")
            checkCorrectInput()
            
    else:
        checkIfGameIsOver()
        

def playerTurn(turn):
    playerTurns.append(turn)
    changeGridX(turn, gridLocal)    
    printGrid(gridLocal)
    checkIfGameIsOver()
    checkForComputer()

def checkForComputer():
    if(checkDraw() == False):
        x = randint(1,9)
        
        if(x in computerTurns):
            checkForComputer()

        elif(x in playerTurns):
            checkForComputer()
            
        else:
            computerTurn(x)
            
    else:
        checkIfGameIsOver()

def computerTurn(turn):
    print("Computer's Turn:")
    computerTurns.append(turn)
    changeGridO(turn, gridLocal)    
    printGrid(gridLocal)
    checkIfGameIsOver()
    checkCorrectInput()

    
def checkIfGameIsOver():
    winningCombinations = [[1,2,3],[1,4,7],[1,5,9],[2,5,8],[3,6,9],[3,5,7],[4,5,6],[7,8,9]]
    for i in winningCombinations:
        if(sublist(i,playerTurns) == True):
            playerWins()               
        if(sublist(i,computerTurns) == True):
            computerWins()
        elif(checkDraw() == True):
            draw()    
        else:
            pass    

def checkDraw():
    listSum = playerTurns + computerTurns
    ls = [1,2,3,4,5,6,7,8,9]
    x = 0

    for i in ls:
        if(i in listSum):
            x = x + 1
        else:
            x = x
    if(x == 9):
        return(True)
    else:
        return(False)


def sublist(lst1, lst2):
    x = 0 
    for element in lst1:
        if(element in lst2):
            x = x + 1
        else:
            x = x

    if(x == 3):
        return(True)
    else:
        return(False)

def playerWins():
    print("Player Wins!")
    endGame()

def computerWins():
    print("Computer Wins!")
    endGame()

def draw():
    print("It's a draw")
    endGame()

def endGame():
    print("Thanks for playing!")
    playAgain()

def playAgain():

    print("Play again? [y/n]")
    answer = input()

    if(answer == "y"):
        system("python3 tictactoe.py")
        exit()

    elif(answer == "n"):
        clear()
        print('''Thanks for Playing
Game Made By Antailbaxt3r''')
        exit()

    else:
        print("Invalid Input")
        playAgain()

startGame()