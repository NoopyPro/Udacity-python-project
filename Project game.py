# Imports modules.
import useful
import random


# Code for attacking.
def fight():
    useful.colored_text("'The troll raises his fist to attack what do you do?'","yellow")
    useful.print_pause("(1)Dodge.")
    useful.print_pause("(2)Attack with the small knife.")
    useful.print_pause("(3)Run.")
    answer = input("(1,2,3): ").lower()
    if answer == "1":
        useful.colored_text("'You attempt to dodge the troll's attack'","yellow")
        useful.colored_text("'But it's too big and your crushed and die instantly.'","yellow")
    elif answer == "2":
        useful.colored_text("'You swing your knife with all of your strength'","yellow")
        useful.colored_text("'But it breaks not making a dent and you're crushed.'","yellow")
    elif answer == "3":
        useful.colored_text("'You turn around and run'","yellow")
        useful.colored_text("'And you manage to leave the troll's cave'","yellow")
        useful.colored_text("'You return to the village'","yellow")
        useful.colored_text("'But instead of a warm welcome you're faced with a trial to be executed.'","yellow")
        useful.colored_text("'days later you are executed due to leaving the quest you had accepted'","yellow")
    else:
        pass

# Main game code.
def main_game():
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
    game_phase = "number Q"
    game_running = True
    game = random.choice(["questionare","fruit catch","taxes"])
    current_question = 1
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
                fight()
                game_phase = "end"
            elif answer == "2" or answer == str(number):
                useful.colored_text("Troll:'Yes that's right!, on to the next game.'","green")
                game_phase = "1st game"
            elif answer == "3":
                useful.colored_text("Troll:'Abraham Lincoln, the 16th President of the United States,\nhe guided the nation through the Civil War\nand abolished slavery with the Emancipation Proclamation,\nultimately becoming an enduring symbol of freedom and equality.'","green")
                useful.colored_text("Troll:'but he is not the correct answer.'","green")
                fight()
                game_phase = "end"
            else:
                useful.colored_text("Troll:'No that's wrong.'","green")
                fight()
                game_phase = "end"
        # Starts the 1st game.
        elif game_phase == "1st game":
            if game == "questionare":
                useful.colored_text("Troll:'Now the game that we'll play is a questionare'","green")
                useful.colored_text("Troll:'I'll ask you three questions'","green")
                useful.colored_text("Troll:'if you get them all right I'll leave the village alone'","green")
                useful.colored_text("Troll:'but if you get one wrong you die.'","green")
                useful.colored_text("Troll:'Okay ready, here's the 1st question.'","green")
                if current_question == 1:

                    question1 = random.choice(["What is the capital city of Japan?","Who is the author of the Harry Potter book series?","Which planet is known as the Red Planet?"])
                    useful.colored_text("Troll:'"+question1+"'","green")
                    if question1 == "What is the capital city of Japan?":
                        useful.print_pause("(1)Tokyo.")
                        useful.print_pause("(2)Kyoto.")
                        useful.print_pause("(3)Mushroom Kingdom.")
                        answer = input("(1/2/3): ").lower()
                        if answer == "1":
                            pass
                        elif answer == "2":
                            pass
                        elif answer == "3":
                            pass
                        else:
                            pass
                    elif question1 == "Who is the author of the Harry Potter book series?":
                        useful.print_pause("(1)J.K. Rowling.")
                        useful.print_pause("(2)Stephen King.")
                        useful.print_pause("(3)Dumbledore the Wizard.")
                        answer = input("(1/2/3): ").lower()
                        if answer == "1":
                            pass
                        elif answer == "2":
                            pass
                        elif answer == "3":
                            pass
                        else:
                            pass
                    elif question1 == "Which planet is known as the Red Planet?":
                        useful.print_pause("(1)Mars.")
                        useful.print_pause("(2)Venus.")
                        useful.print_pause("(3)Strawberry.")
                        answer = input("(1/2/3): ").lower()
                        if answer == "1":
                            pass
                        elif answer == "2":
                            pass
                        elif answer == "3":
                            pass
                        else:
                            pass
            elif game == "fruit catch":
                pass
            elif game == "taxes":
                pass

        # Plays this code at the end of the game.
        elif game_phase == "end":
            useful.colored_text("'Do you want to play again?'","light grey")
            useful.print_pause("(1)Yes.")
            useful.print_pause("(2)No.")
            answer = input("(1/2): ").lower()
            if answer == "1":
                useful.colored_text("'Okay let's play.'","light grey")
                game = random.choice(["questionare","fruit catch","taxes"])
                game_phase = "number Q"
            elif answer == "2":
                print("'okay.'")
                game_running = False

# Starts game.
main_game()