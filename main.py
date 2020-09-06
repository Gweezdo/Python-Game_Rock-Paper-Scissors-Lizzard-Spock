# This is a python implementation of the game Rock Paper Scissors Lizzard Spock as introduced my television series Big Bang Theory.

import random


def game_logic(user_choice, computer_choice):
    if(user_choice == computer_choice):
        return 0
    #user win    
    elif(user_choice == "Rock" and (computer_choice == "Scissors" or computer_choice == "Lizard")):
        return 1
    elif(user_choice == "Paper" and (computer_choice == "Rock" or computer_choice == "Spock")):
        return 1
    elif(user_choice == "Scissors" and (computer_choice == "Lizard" or computer_choice == "Paper")):
        return 1
    elif(user_choice == "Lizard" and (computer_choice == "Spock" or computer_choice == "Paper")):
        return 1
    elif(user_choice == "Spock" and (computer_choice == "Rock" or computer_choice == "Scissors")):
        return 1
    #computer win    
    elif(computer_choice == "Rock" and (user_choice == "Scissors" or user_choice == "Lizard")):
        return -1
    elif(computer_choice == "Paper" and (user_choice == "Rock" or user_choice == "Spock")):
        return -1
    elif(computer_choice == "Scissors" and (user_choice == "Lizard" or user_choice == "Paper")):
        return -1
    elif(computer_choice == "Lizard" and (user_choice == "Spock" or user_choice == "Paper")):
        return -1
    elif(computer_choice == "Spock" and (user_choice == "Rock" or user_choice == "Scissors")):
        return -1

#Com Putera's guess
def computer_guess_func():
    object_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    random_int = random.randint(0,4)
    return object_list[random_int]

#Game start screen
def mainGame():
    username = input("Welcome to Rock Paper Scissors Lizard Spock! \nPlease enter your character name: ")
    print("\n")
    game_rounds = input("Hi " + username + ", how many rounds do you want to play? (3, 5, 10, 100 etc): ")

    game_rounds_flag = True
    while(game_rounds_flag):
        game_rounds_flag = False
        if (game_rounds.isdigit()):
            game_rounds = int(game_rounds)
            break
        elif(game_rounds_flag == "0"):
            game_rounds_flag = True
            game_rounds = input("Oops! That is not the input we were expecting. Please enter an whole number greater than or equal to '1': ")
        else:
            game_rounds_flag = True
            game_rounds = input("Oops! That is not the input we were expecting. Please enter an whole number greater than or equal to '1': ")

    print("You have selected to play " + str(game_rounds) + " rounds against the evil Com Putera!")
    print("\n")

#Game objective

    
    game_objective = input("Do you want to see the rules of the game? Enter 'Y' for Yes or 'N' for No: ")
    game_objective_flag = True
    while(game_objective_flag):
        game_objective_flag = False
        if(game_objective.lower() == 'y'):
            print("\n")
            print("The objective of the game is to beat the evil Com Putera by playing one of the 5 objects (Rock, Paper, Scissors, Lizard, Spock).\nEach object defeats 2 other objects and can be deafeated by 2 other objects.\nScissors cuts Paper \nPaper covers Rock \nRock crushes Lizard \nLizard poisons Spock \nSpock smashes Scissors \nScissors decapitates Lizard \nLizard eats Paper \nPaper disproves Spock \nSpock vaporises Rock and as it always has, \nRock crushed Scissors")    
            print("\n")
            break
        elif(game_objective.lower() == 'n'):
            continue
        else:
            game_objective = input("Oops, that was unexpected input! To see the rules of the game enter 'Y' for Yes or 'N' for No : ")
            print("\n")
            game_objective_flag = True
        



#Main game loop
    computer_total = 0
    user_total = 0
    tie_total = 0

    rounds = range(game_rounds)
    for i in rounds:
        
        computer_guess = computer_guess_func()

        print("Round " + str(i+1) + " of " + str(game_rounds))
        user_input = input("Please Enter: \n'R' for Rock, 'P' for Paper, 'S' for Scissors, 'L' for Lizard or 'SP' for Spock (or 'Q' to quit the game): ")
        
        user_input_flag = True
        while(user_input_flag):
            user_input_flag = False
            user_choice = ''
            if(user_input.lower() == "r"):
                user_choice = 'Rock'
            elif(user_input.lower() == "p"):
                user_choice = 'Paper'
            elif(user_input.lower() == "s"):
                user_choice = 'Scissors'
            elif(user_input.lower() == "l"):
                user_choice = 'Lizard'
            elif(user_input.lower() == "sp"):
                user_choice = 'Spock'
            elif(user_input.lower() == "q"):
                user_choice = 'Quit'
                break    
            else:
                user_input_flag = True
                user_input = input("Oops, unexpected input! Please Enter: \n'R' for Rock, 'P' for Paper, 'S' for Scissors, 'L' for Lizzard or 'SP' for Spock (or 'Q' to quit the game): ")
                
        if(user_choice == "Quit"):
            print("Goodbye!")
            break
        else:        
            print("Com Putera choose " + computer_guess)
            print(username + " choose " + user_choice)    
            win_lose_tie = game_logic(user_choice, computer_guess)

            if(win_lose_tie == -1):
                print("Com Putera wins the round!")
                computer_total +=1
            elif(win_lose_tie == 0):
                tie_total +=1
                print("It's a Tie! No points assigned")
            elif(win_lose_tie == 1):
                user_total +=1
                print(username + " wins the round!")  

        print("\n")  

    print("Final score's are as follow: \n")
    print(username + " = " + str(user_total) + " points")
    print("Com Putera = " + str(computer_total) + " points")
    print("Ties = " + str(tie_total))

    if(user_total > computer_total):
        print("Overall winner of the match is " + username + "!")
    elif(user_total < computer_total):
        print("Overall winner of the match is Com Putera!")
    elif(user_total == computer_total and user_choice != "Quit"):
        print("It's a TIE!!")    

mainGame()
