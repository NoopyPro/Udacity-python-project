import turtle
import keyboard
import random
import winsound
import math
import time

# Global variables
score = 0
damage = 0
kills = 0
player = None
weapon = None
enemy = None

# Prints a string with delay and space after
def print_pause(string):
    time.sleep(2.5)
    print(string)
    print("")

# Function to setup game environment
def setup_game():
    global score, damage, kills, player, weapon, enemy
    
    screen = turtle.Screen()
    screen.clear()
    screen.bgcolor("green")

    # Create player turtle
    player = turtle.Turtle()
    player.shape("turtle")
    player.penup()
    
    # Create weapon turtle
    weapon = turtle.Turtle()
    weapon.color("red")
    weapon.penup()
    
    # Create enemy turtle
    enemy = turtle.Turtle()
    enemy.penup()
    enemy.color("blue")
    enemy.goto(random.randint(-200, 200), random.randint(-200, 200))

    # Reset global variables
    score = 0
    damage = 0
    kills = 0

# Checks for weapon hits
def weapon_hit():
    global score, damage
    if weapon.distance(enemy) < 10:
        damage += 1
        score += 1
        winsound.Beep(600, 500)

# Function for player movement and attack
def player_moves():
    global player, weapon
    
    weapon.color("red") 
    weapon.goto(player.position())
    weapon.setheading(player.heading())

    if keyboard.is_pressed("right"):
        player.setheading(0)
        player.forward(6)
    elif keyboard.is_pressed("left"):
        player.setheading(180)
        player.forward(6)
    elif keyboard.is_pressed("up"):
        player.setheading(90)
        player.forward(6)
    elif keyboard.is_pressed("down"):
        player.setheading(270)
        player.forward(6)

    elif keyboard.is_pressed("a"):
        weapon.setheading(player.heading())
        weapon.forward(40)
        weapon_hit()
        weapon.left(90)
        weapon.forward(20)
        weapon_hit()
        weapon.setheading(player.heading())
        weapon.right(90)
        weapon.pendown()
        weapon.forward(40)
        weapon.penup()
        weapon_hit()
        weapon.goto(player.position())
        weapon.color("green")
        weapon.setheading(player.heading())
        weapon.forward(40)
        weapon.left(90)
        weapon.forward(20)
        weapon.setheading(player.heading())
        weapon.right(90)
        weapon.pendown()
        weapon.forward(40)
        weapon.penup()
        weapon.goto(player.position())

# Simple enemy moves toward player
def enemy_movement():
    global enemy, damage, kills, player
    
    enemy_direction = math.degrees(math.atan2(player.ycor() - enemy.ycor(), player.xcor() - enemy.xcor()))
    enemy.setheading(enemy_direction)
    enemy.forward(5)
    if damage == 3:
        kills += 1
        damage = 0
        enemy.goto(random.randint(-200, 200), random.randint(-200, 200))

# Main game function
def main_game():
    global screen
    
    setup_game()
    kills = 0
    score = 0
    
    while True:
        player_moves()
        enemy_movement()
        
        # Game over condition
        if player.distance(enemy) < 20 and player.position() != (0, 0):
            screen.textinput("Game Over!,","You lost!, Your score: " + str(score) + ", Number of kills: " + str(kills) + ", Press OK to exit")
            # Ask if player wants to play again
            play_again = screen.textinput("Play Again?", "Do you want to play again? (y/n):")
            if play_again and play_again.lower() in ["y", "yes"]:
                # Reset any game state variables if needed
                main_game()
            else:
                print_pause("Okay, hope you come play again.")
                turtle.bye()
                break
        
        # Check if player wants to end the game
        if keyboard.is_pressed("esc"):
            print_pause("Game ended by user.")
            turtle.bye()
            break

        # Win condition
        if kills == 5:
            screen.textinput("You won!", "Congratulations! Press OK to exit.")
            # Ask if player wants to play again
            play_again = screen.textinput("Play Again?", "Do you want to play again? (y/n):")
            if play_again and play_again.lower() in ["y", "yes"]:
                # Reset any game state variables if needed
                main_game()
            else:
                print("")
                print_pause("Okay, hope you come play again.")
                turtle.bye()
                break

# Game instructions
screen = turtle.Screen()
screen.setup(width=1.0,height=1.0)
screen.textinput("Instructions", "You play the game using arrow keys to move and 'a' key to attack blue enemies. Avoid touching enemies to stay alive. Kill an enemy by hitting it 3 times. Win by killing 5 enemies. Good luck! Press OK to start.")

# Start the game
main_game()
