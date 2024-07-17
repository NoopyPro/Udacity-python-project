# Imports modules.
import random
import time


# ANSI color codes for foreground text colors
class colors:
    """ ANSI color codes """
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"  # Reset to default color

# Prints entered string with a pause.
def print_pause(string:str):
    print("")
    print(string)
    time.sleep(2)

# Prints enteres string with a pause and colour.
def colored_text(string: str, color: str):
    print("")
    color = color.lower()
    if color == "black":
        print(colors.BLACK + string + colors.END)
    elif color == "red":
        print(colors.RED + string + colors.END)
    elif color == "green":
        print(colors.GREEN + string + colors.END)
    elif color == "brown":
        print(colors.BROWN + string + colors.END)
    elif color == "blue":
        print(colors.BLUE + string + colors.END)
    elif color == "purple":
        print(colors.PURPLE + string + colors.END)
    elif color == "magenta":
        print(colors.MAGENTA + string + colors.END)
    elif color == "cyan":
        print(colors.CYAN + string + colors.END)
    elif color == "white":
        print(colors.WHITE + string + colors.END)
    elif color == "light gray":
        print(colors.LIGHT_GRAY + string + colors.END)
    elif color == "dark gray":
        print(colors.DARK_GRAY + string + colors.END)
    elif color == "light red":
        print(colors.LIGHT_RED + string + colors.END)
    elif color == "light green":
        print(colors.LIGHT_GREEN + string + colors.END)
    elif color == "yellow":
        print(colors.YELLOW + string + colors.END)
    elif color == "light blue":
        print(colors.LIGHT_BLUE + string + colors.END)
    elif color == "light purple":
        print(colors.LIGHT_PURPLE + string + colors.END)
    elif color == "light cyan":
        print(colors.LIGHT_CYAN + string + colors.END)
    elif color == "light white":
        print(colors.LIGHT_WHITE + string + colors.END)
    elif color == "bold":
        print(colors.BOLD + string + colors.END)
    elif color == "faint":
        print(colors.FAINT + string + colors.END)
    elif color == "italic":
        print(colors.ITALIC + string + colors.END)
    elif color == "underline":
        print(colors.UNDERLINE + string + colors.END)
    elif color == "blink":
        print(colors.BLINK + string + colors.END)
    elif color == "negative":
        print(colors.NEGATIVE + string + colors.END)
    elif color == "crossed":
        print(colors.CROSSED + string + colors.END)
    elif color == "reset":
        print(string + colors.END)
    else:
        print(string + colors.END)
    time.sleep(1.6)

# Code for attacking.
def fight():
    colored_text("'The troll raises his fist to attack what do you do?'","yellow")
    print_pause("(1)Dodge.")
    print_pause("(2)Attack with the small knife.")
    print_pause("(3)Run.")
    answer = input("(1,2,3): ").lower()
    if answer == "1":
        colored_text("'You attempt to dodge the troll's attack'","yellow")
        colored_text("'But it's too big and your crushed and die instantly.'","yellow")
    elif answer == "2":
        colored_text("'You swing your knife with all of your strength'","yellow")
        colored_text("'But it breaks not making a dent and you're crushed.'","yellow")
    elif answer == "3":
        colored_text("'You turn around and run'","yellow")
        colored_text("'And you manage to leave the troll's cave'","yellow")
        colored_text("'You return to the village'","yellow")
        colored_text("'But instead of a warm welcome you're faced with a trial to be executed.'","yellow")
        colored_text("'days later you are executed due to leaving the quest you had accepted'","yellow")
    else:
        colored_text("'You're crushed and die instantly.'","yellow")

# Main game code.
def main_game():
    # Game opening.
    colored_text("'Your a hero that travels the land looking for work'","yellow")
    colored_text("'Having no food you take any jobs you can'","yellow")
    colored_text("'You're asked to deal with a troll near a village'","yellow")
    colored_text("'You enter the cave weilding nothing but your wit and a small knife.'","yellow")
    colored_text("Troll:'You dare to uhh umm hmmm'","green")
    colored_text("Troll:'You know what.'","green")
    colored_text("Troll:'I'm kinda bored so let's play a game.'","green")
    colored_text("Troll:'I'll ask you a question'","green")
    colored_text("Troll:'if you answer right then you'll play the next game'","green")
    colored_text("Troll:'if you answer wrong I'll kill you'","green")
    colored_text("Troll:'Okay,ready...'","green")

    # Riddles.
    riddles = [
    {"question": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?",
    "options": ["(1) Echo", "(2) Whisper", "(3) Sound"],
    "answer": "1"},
                    
    {"question": "What has keys but can't open locks?",
    "options": ["(1) Keyboard", "(2) Locksmith", "(3) Piano"],
    "answer": "1"},
                    
    {"question": "The more you take, the more you leave behind. What am I?",
    "options": ["(1) Time", "(2) Footsteps", "(3) Memories"],
    "answer": "2"}
    ]

    game_phase = "number Q"
    game_running = True
    game = random.choice(["riddles","fruit catch","taxes"])

    # Main game loop.
    while game_running == True:
        # Number question game phase.
        if game_phase == "number Q":
            number = random.randint(2,1000)
            colored_text("Troll:'What's a number between " + str(number - 1) + " and " + str(number + 1) + "?'","green")
            print_pause("(1)"+str(number / 3)+".")
            print_pause("(2)"+str(number)+".")
            print_pause("(3)Abraham Lincoln.")
            answer = input("(1,2,3): ").lower()
            if answer == "1":
                colored_text("Troll:'No that's wrong.'","green")
                fight()
                game_phase = "end"
            elif answer == "2" or answer == str(number):
                colored_text("Troll:'Yes that's right!, on to the next game.'","green")
                game_phase = "1st game"
            elif answer == "3":
                colored_text("Troll:'Abraham Lincoln, the 16th President of the United States,\nhe guided the nation through the Civil War\nand abolished slavery with the Emancipation Proclamation,\nultimately becoming an enduring symbol of freedom and equality.'","green")
                colored_text("Troll:'but he is not the correct answer.'","green")
                fight()
                game_phase = "end"
            else:
                colored_text("Troll:'No that's wrong.'","green")
                fight()
                game_phase = "end"
        # Starts the 1st game.
        elif game_phase == "1st game":
            if game == "riddles":# Riddle Challenge mini-game 
                colored_text("Troll:'Welcome to the Riddle Challenge!'", "green")
                colored_text("Troll:'I will ask you three riddles.'", "green")
                colored_text("Troll:'Choose the correct answer from the given options or die.'", "green")
                
                score = 0
                
                # Asks riddle questions.
                for riddle in riddles:
                    colored_text("Troll:'"+ riddle['question'] + "'","green")
                    for option in riddle['options']:
                        print_pause(option)
                    
                    answer = input("Your answer (1,2,3): ").strip().upper()
                    
                    if answer == riddle['answer']:
                        colored_text("Troll:'Correct!'", "green")
                        score += 1
                    else:
                        colored_text("'The troll is not pleased with your answer!'", "yellow")
                        fight()
                        game_phase = "end"
                        break

                    if score >= 3:
                        colored_text("Troll:'You win I'll leave the village alone.'","green")
                        colored_text("'You leave the troll's cave and collect the quest reward,'","yellow")
                        colored_text("'You go to eat before going onto the next job.'","yellow")
                        game_phase = "end"

            elif game == "fruit catch":
                colored_text("Troll:'In this I will throw fruit at you.'","green")
                colored_text("Troll:'And you will try and catch it'","green")
                colored_text("Troll:'Okay,ready...'","green")
                colored_text("Troll:'GO!'","green")

                score = 0

                for i in range(3):
                    colored_text("'The troll throws a fruit at you hit enter when the light is green.'","yellow")
                    time.sleep(random.randint(1,10))
                    start_time = time.time()
                    colored_text("'NOW!'","light green")
                    input()
                    end_time = time.time()
                    if abs(end_time-start_time) >= 2:
                        colored_text("'You don't catch the fruit and it hits you on the head and breaks your skull.'","yellow")
                        game_phase = "end"
                        break
                    else:
                        colored_text("'You catch the fruit.'","yellow")
                        score += 1

                    if score >= 3:
                        colored_text("Troll:'You win I'll leave the village alone.'","green")
                        colored_text("'You leave the troll's cave and collect the quest reward,'","yellow")
                        colored_text("'You go to eat before going onto the next job.'","yellow")
                        game_phase = "end"

            elif game == "taxes":
                colored_text("Troll:'Time to talk taxes!'","green")
                colored_text("Troll:'You owe me 100 gold coins as tax for passing through my territory.'","green")
                
                print_pause("You check your inventory and see you have:")
                print_pause("- 80 gold coins")
                print_pause("- A valuable gem worth 50 gold coins")
                print_pause("- A magic potion worth 100 gold coins")

                colored_text("Troll:'Choose how you will pay your taxes:'", "green")
                print_pause("(1) 80 gold coins")
                print_pause("(2) Valuable gem worth 50 gold coins")
                print_pause("(3) Magic potion worth 100 gold coins")

                answer = input("Your choice (1, 2, 3): ").strip().lower()

                if answer == "1":
                    colored_text("Troll:'You're short by 20 gold coins. Pay up!'","green")
                    fight()
                    game_phase = "end"
                elif answer == "2":
                    colored_text("Troll:'That's not enough! You're trying to trick me.'","green")
                    fight()
                    game_phase = "end"
                elif answer == "3":
                    colored_text("Troll:'Very well, that potion will do. You may pass.'","green")
                    colored_text("'You leave the troll's cave and collect the quest reward,'","yellow")
                    colored_text("'You go to eat before going onto the next job.'","yellow")
                    game_phase = "end"
                else:
                    colored_text("Troll:'I don't have all day. Choose now!'","green")
                    fight()
                    game_phase = "end"

        # Plays this code at the end of the game.
        elif game_phase == "end":
            colored_text("'Do you want to play again?'","light grey")
            print_pause("(1)Yes.")
            print_pause("(2)No.")
            answer = input("(1/2): ").lower()
            if answer == "1":
                colored_text("'Okay let's play.'","light grey")
                game = random.choice(["riddles","fruit catch","taxes"])
                game_phase = "number Q"
            elif answer == "2":
                print("'okay.'")
                game_running = False

# Starts game.
main_game()