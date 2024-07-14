# Imports modules.
import useful
import random


# Code for attacking.
def fight():
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
    number = random.randint(2,1000)
    useful.colored_text("Troll:'What's a number between " + str(number - 1) + " and " + str(number + 1) + "?'","green")
    useful.print_pause("(1)"+str(number / 3)+".")
    useful.print_pause("(2)"+str(number)+".")
    useful.print_pause("(3)Abraham Lincoln.")
    answer = input("(1,2,3):").lower()
    if answer == "1":
        useful.colored_text("Troll:'No that's wrong.'","green")
        fight()
    elif answer == "2":
        useful.colored_text("Troll:'Yes that's right!, on to the next game.'","green")
    elif answer == "3":
        useful.colored_text("Troll:'Abraham Lincoln, the 16th President of the United States,\nguided the nation through the Civil War\nand abolished slavery with the Emancipation Proclamation,\nultimately becoming an enduring symbol of freedom and equality.'","green")
        useful.colored_text("Troll:'but he is not the correct answer.'","green")


# Starts game.
main_game()