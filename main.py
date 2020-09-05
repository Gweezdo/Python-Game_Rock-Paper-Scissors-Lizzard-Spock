# This is a python implementation of the game Rock Paper Scissors Lizzard Spock as introduced my television series Big Bang Theory.

#Game start screen
def mainGame():
    username = input("Welcome to Rock Paper Scissors Lizard Spock! \nPlease enter your character name: ")
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

    
mainGame()
