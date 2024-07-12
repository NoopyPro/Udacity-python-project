# Import modules.
import turtle
import keyboard
import random
import winsound
import math
import time

# Prints a string with delay and space after
def print_pause(string):
    time.sleep(1.5)
    print(string)
    print("")

# Function to setup game environment
def setup_game():
    screen.bgcolor("green")

    global score, damage, kills

    global player, weapon, enemy
    
    # Create player turtle
    player = turtle.Turtle()
    player.shape("turtle")
    player.penup()

    # Global variables
    score = 0
    damage = 0
    kills = 0
    
    # Create weapon turtle
    weapon = turtle.Turtle()
    weapon.color("red")
    weapon.penup()
    
    # Create enemy turtle
    enemy = turtle.Turtle()
    enemy.penup()
    enemy.color("blue")
    enemy.goto(random.randint(-200, 200), random.randint(-200, 200))

# Checks for weapon hits.
def weapon_hit():
    global score, damage
    if weapon.distance(enemy) < 10:
        damage += 1
        score += 1
        winsound.Beep(600, 500)

# Function for player movement and attack.
def player_moves():
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

# Simple enemy moves toward player.
def enemy_movement():
    global damage,kills
    enemy_direction = math.degrees(math.atan2(player.ycor() - enemy.ycor(), player.xcor() - enemy.xcor()))
    enemy.setheading(enemy_direction)
    enemy.forward(5)
    if damage == 3:
        kills += 1
        damage = 0
        enemy.goto(random.randint(-200, 200), random.randint(-200, 200))

# Main game function.
def main_game():
    
    setup_game()
    
    while True:
        player_moves()
        enemy_movement()
        
        if player.distance(enemy) < 20 and player.position() != (0, 0):
            print("Game Over!")
            break
        
        if keyboard.is_pressed("esc"):
            print("Game ended by user.")
            break

        if kills == 5:
            print("You won")
            break
    
    print("")
    print_pause("Your score: " + str(score))
    print_pause("Number of kills: " + str(kills))
    
    # Ask if player wants to play again.
    player_input = input("Do you want to play again (y/n): ").lower()
    if player_input in ["y", "yes"]:
        print("")
        print("Go to the turtle app.")
        screen.clear()  # Clear the screen
        main_game()
    else:
        print("")
        print_pause("Okay, hope you come play again.")
        turtle.bye()

# Start the game
print_pause("You play the game by using the arrow keys to move,")
print_pause("and using the 'a' key to attack an enemy that is blue")
print_pause("if an enemy touches you, you lose")
print_pause("you can kill an enemy by hitting it 3 times")
print_pause("if you kill an enemy 5 times you win")
print_pause("Now good luck.")

# Create a turtle screen
screen = turtle.Screen()
screen.setup(width=1.0,height=1.0)
screen.bgcolor("green")

main_game()
