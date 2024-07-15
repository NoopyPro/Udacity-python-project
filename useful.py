import time
import random

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