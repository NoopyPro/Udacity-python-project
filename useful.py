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

def print_pause(string:str):
    print("")
    print(string)
    time.sleep(2)

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
