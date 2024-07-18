import time
import random

# Function to print with a pause for readability
def print_pause(string):
    time.sleep(2)
    print(string)
    print("")

# Function to get the player's guess (1, 2, 3, or 4)
def get_player_guess():
    while True:
        player_guess = input("What number do you guess (1, 2, 3, or 4)? ")
        print("")
        if player_guess.lower() in ["1", "2", "3", "4"]:
            return player_guess
        else:
            print("Please guess a number in 1, 2, 3, or 4.\n")

# Function to introduce the game
def introduction():
    print_pause("You sit in front of a man that says:")
    print_pause("'So you've come to try and beat me'")
    print_pause("'okay'")
    print_pause("'The game's objective is to gain 5 points'")
    print_pause("'by guessing a number that is in 1, 2, 3, or 4'")
    print_pause("'I choose which number is correct'")
    print_pause("'but I cannot choose the same number 2 times in a row'")
    print_pause("'you gain points by guessing right'")
    print_pause("'and lose points by guessing wrong'")
    print_pause("'You have 2 things to help you'")
    print_pause("'The 'White flag' skips your turn and changes my choice,'")
    print_pause("'And the 'Double-edged knife' allows gaining 2 points'")
    print_pause("'if you guess right but you'll lose if you guess wrong.'")
    print("")

# Function to ask the player if they want to play
def ask_to_play():
    while True:
        player_command = input("Do you wish to play? (yes/no) ").lower()
        if player_command in ["yes", "y"]:
            print("Okay, let's start.")
            return True
        elif player_command in ["no", "n"]:
            print("'Okay, hopefully you'll play again.'")
            time.sleep(2)
            exit()
        else:
            print("Please enter yes or no.\n")

# Game logic
def main_game():
    player_score = 0
    last_choice = None
    
    introduction()
    
    if not ask_to_play():
        return
    
    print("Input 1 to guess,")
    print("Input 2 to use the white flag,")
    print("Input 3 to use the double-edged knife.")
    
    # Main game loop runs until player_score reaches 5
    while player_score < 5:
        
        # Ensure player_score does not go below 0
        if player_score < 0:
            player_score = 0
        
        # Dad's choice of a number (1, 2, 3, or 4)
        dad_choice = random.choice(["1", "2", "3", "4"])
        while dad_choice == last_choice:
            dad_choice = random.choice(["1", "2", "3", "4"])
        last_choice = dad_choice
        
        print("Your score is " + str( player_score))
        print_pause("'What do you do?'")
        
        player_turn = True
        while player_turn:
            # Player chooses their action
            player_command = input("Input: ").lower()
            print("")
            
            if player_command == "1":
                # Player chooses to guess a number
                player_guess = get_player_guess()
                if player_guess == dad_choice:
                    print_pause("'You guessed right!'")
                    player_score += 1
                    player_turn = False
                else:
                    print_pause("'You guessed wrong!'")
                    player_score -= 1
                    player_turn = False
            
            elif player_command == "2":
                # Player chooses to use the white flag
                print("'Okay, I changed my guess.'")
                player_turn = False
            
            elif player_command == "3":
                # Player chooses to use the double-edged knife
                player_guess = get_player_guess()
                if player_guess == dad_choice:
                    print_pause("'You guessed right!'")
                    player_score += 2
                    player_turn = False
                else:
                    print_pause("'You guessed wrong!'")
                    print_pause("'You lose.'")
                    print("'Hopefully you'll play again.'")
                    time.sleep(2)
                    exit()
            else:
                print("Please input 1,2 or 3.")
    
    # If the player wins
    print_pause("'Okay, you won! Good game, son.'")
    print_pause("'As a reward, let's go out for ice cream.'")

    while True:
        player_command = input("Do you want to play again? (yes/no) ").lower()
        if player_command in ["yes", "y"]:
            main_game()
        elif player_command in ["no", "n"]:
            exit()
        else:
            print_pause("'Please tell me if you want to play again'")

# Start the game by calling the main_game function
main_game()
