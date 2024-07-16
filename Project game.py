# Imports modules.
import useful
import random
import time


# Main game code.
def main_game():
    # Game opening.
    useful.colored_text("'Your a hero that travels the land looking for work'","yellow")
    useful.colored_text("'Having no food you take any jobs you can'","yellow")
    useful.colored_text("'You're asked to deal with a troll near a village'","yellow")
    useful.colored_text("'You enter the cave weilding nothing but your wit and a small knife.'","yellow")
    useful.colored_text("Troll:'You dare to uhh umm hmmm'","green")
    useful.colored_text("Troll:'You know what.'","green")
    useful.colored_text("Troll:'I'm kinda bored so let's play a game.'","green")
    useful.colored_text("Troll:'I'll ask you a question'","green")
    useful.colored_text("Troll:'if you answer right then you'll play the next game'","green")
    useful.colored_text("Troll:'if you answer wrong I'll kill you'","green")
    useful.colored_text("Troll:'Okay,ready...'","green")

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
            useful.colored_text("Troll:'What's a number between " + str(number - 1) + " and " + str(number + 1) + "?'","green")
            useful.print_pause("(1)"+str(number / 3)+".")
            useful.print_pause("(2)"+str(number)+".")
            useful.print_pause("(3)Abraham Lincoln.")
            answer = input("(1,2,3): ").lower()
            if answer == "1":
                useful.colored_text("Troll:'No that's wrong.'","green")
                useful.fight()
                game_phase = "end"
            elif answer == "2" or answer == str(number):
                useful.colored_text("Troll:'Yes that's right!, on to the next game.'","green")
                game_phase = "1st game"
            elif answer == "3":
                useful.colored_text("Troll:'Abraham Lincoln, the 16th President of the United States,\nhe guided the nation through the Civil War\nand abolished slavery with the Emancipation Proclamation,\nultimately becoming an enduring symbol of freedom and equality.'","green")
                useful.colored_text("Troll:'but he is not the correct answer.'","green")
                useful.fight()
                game_phase = "end"
            else:
                useful.colored_text("Troll:'No that's wrong.'","green")
                useful.fight()
                game_phase = "end"
        # Starts the 1st game.
        elif game_phase == "1st game":
            if game == "riddles":# Riddle Challenge mini-game 
                useful.colored_text("Troll:'Welcome to the Riddle Challenge!'", "green")
                useful.colored_text("Troll:'I will ask you three riddles.'", "green")
                useful.colored_text("Troll:'Choose the correct answer from the given options or die.'", "green")
                
                score = 0
                
                # Asks riddle questions.
                for riddle in riddles:
                    useful.colored_text("Troll:'"+ riddle['question'] + "'","green")
                    for option in riddle['options']:
                        useful.print_pause(option)
                    
                    answer = input("Your answer (1,2,3): ").strip().upper()
                    
                    if answer == riddle['answer']:
                        useful.colored_text("Troll:'Correct!'", "green")
                        score += 1
                    else:
                        useful.colored_text("'The troll is not pleased with your answer!'", "yellow")
                        useful.fight()
                        game_phase = "end"
                        break

                    if score >= 3:
                        useful.colored_text("Troll:'You win I'll leave the village alone.'","green")
                        useful.colored_text("'You leave the troll's cave and collect the quest reward,'","yellow")
                        useful.colored_text("'You go to eat before going onto the next job.'","yellow")
                        game_phase = "end"

            elif game == "fruit catch":
                useful.colored_text("Troll:'In this I will throw fruit at you.'","green")
                useful.colored_text("Troll:'And you will try and catch it'","green")
                useful.colored_text("Troll:'Okay,ready...'","green")
                useful.colored_text("Troll:'GO!'","green")

                score = 0

                for i in range(3):
                    useful.colored_text("'The troll throws a fruit at you hit enter when the light is green.'","yellow")
                    time.sleep(random.randint(1,10))
                    start_time = time.time()
                    useful.colored_text("'NOW!'","light green")
                    input()
                    end_time = time.time()
                    if abs(end_time-start_time) >= 2:
                        useful.colored_text("'You don't catch the fruit and it hits you on the head and breaks your skull.'","yellow")
                        game_phase = "end"
                        break
                    else:
                        useful.colored_text("'You catch the fruit.'","yellow")
                        score += 1

                    if score >= 3:
                        useful.colored_text("Troll:'You win I'll leave the village alone.'","green")
                        useful.colored_text("'You leave the troll's cave and collect the quest reward,'","yellow")
                        useful.colored_text("'You go to eat before going onto the next job.'","yellow")
                        game_phase = "end"

            elif game == "taxes":
                useful.colored_text("Troll:'Time to talk taxes!'","green")
                useful.colored_text("Troll:'You owe me 100 gold coins as tax for passing through my territory.'","green")
                
                useful.print_pause("You check your inventory and see you have:")
                useful.print_pause("- 80 gold coins")
                useful.print_pause("- A valuable gem worth 50 gold coins")
                useful.print_pause("- A magic potion worth 100 gold coins")

                useful.colored_text("Troll:'Choose how you will pay your taxes:'", "green")
                useful.print_pause("(1) 80 gold coins")
                useful.print_pause("(2) Valuable gem worth 50 gold coins")
                useful.print_pause("(3) Magic potion worth 100 gold coins")

                answer = input("Your choice (1, 2, 3): ").strip().lower()

                if answer == "1":
                    useful.colored_text("Troll:'You're short by 20 gold coins. Pay up!'","green")
                    useful.fight()
                    game_phase = "end"
                elif answer == "2":
                    useful.colored_text("Troll:'That's not enough! You're trying to trick me.'","green")
                    useful.fight()
                    game_phase = "end"
                elif answer == "3":
                    useful.colored_text("Troll:'Very well, that potion will do. You may pass.'","green")
                    useful.colored_text("'You leave the troll's cave and collect the quest reward,'","yellow")
                    useful.colored_text("'You go to eat before going onto the next job.'","yellow")
                    game_phase = "end"
                else:
                    useful.colored_text("Troll:'I don't have all day. Choose now!'","green")
                    useful.fight()
                    game_phase = "end"

        # Plays this code at the end of the game.
        elif game_phase == "end":
            useful.colored_text("'Do you want to play again?'","light grey")
            useful.print_pause("(1)Yes.")
            useful.print_pause("(2)No.")
            answer = input("(1/2): ").lower()
            if answer == "1":
                useful.colored_text("'Okay let's play.'","light grey")
                game = random.choice(["riddles","fruit catch","taxes"])
                game_phase = "number Q"
            elif answer == "2":
                print("'okay.'")
                game_running = False

# Starts game.
main_game()