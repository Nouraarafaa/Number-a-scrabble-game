# File: CS112_A1_T2
# Purpose: each of the 2 players will choose a number 1==>9 and the chosen number will be canceled.
#          If a player has picked three numbers that add up to 15, that player wins the game and if
#          none of them wins the game will draw.
# Author: Noura Muhammad Mahmoud Arafa


#Setting The Variables
numbers_list=[1,2,3,4,5,6,7,8,9]
score1=[]
score2=[]

#function to take an input from player 1
def player1():
    while True:
        global score1
        num1= input("player one enter a number from 1 to 9\n")
        if num1 == "" or len(num1) >= 2:
            continue
        player1_numb = int(num1)
        if player1_numb in numbers_list:
            numbers_list.remove(player1_numb) #to cancel the chosen number from list
            score1.append(player1_numb) # to add the chosen number to the score list
            break
        else:
            print("Error:this number is invalid") #if the player chose a number out of the range from 1==>9
            continue


#function to take an input from player 2
def player2():
    while True:
        global score2
        num2= input("player two a number from 1 to 9\n")
        if num2 == "" or len(num2) >= 2:
            print("Please insert a number between 1 and 9\n")
            continue
        player2_numb = int(num2)
        if player2_numb in numbers_list:
            numbers_list.remove(player2_numb)
            score2.append(player2_numb)
            break
        else:
            print("Error:this number is invalid")
            continue
#function to add the score of each of them to fund the winner
def player_win(score):
    for i1 in score:
        for i2 in score:
            for i3 in score:
                if i1 == i2 or i1 == i3 or i2 == i3:
                    continue
                if i1 + i2 + i3==15:
                    return True
    return False


#function for playing the game
def thegame():
    print("Welcome to Number a Scrabble game")
    print("The list of numbers:",numbers_list)
    while True:
        player1()
        print("The list of numbers:",numbers_list)
        if player_win(score1):
            print("**Player 1 is the winner**")
            break
        if len(numbers_list)==0 : # to check if the number list is empty and now one wins so the game will draw
            print("**Draw**")
            break
        player2()
        print("The list of numbers:",numbers_list)
        if player_win(score2):
            print("**Player 2 is the winner**")
            break
        if len(numbers_list)==0 :
            print("**Draw**")
            break


thegame()




"""
Test Cases:
    player 1 ==>[1 ,6 ,9 ,8 ]
    player 2==>[2 ,3 ,7 ]
    player 1 is the winner


    player 1==>[7 ,8 ,9 ,6 ,5]
    player 2==>[1 ,2 ,3 ,4 ]
    the Game will Draw

    if input player 1 or 2 = Noura or " " 
    output==> enter a number from 1 to 9

"""









