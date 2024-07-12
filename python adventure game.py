import turtle
import keyboard
import random

# Create a turtle screen
screen = turtle.Screen()

# Set background color
screen.bgcolor("green")

# Create a turtle instance
player = turtle.Turtle()
player.shape("turtle")
player.penup()
weapon = turtle.Turtle()
weapon.color("red")
weapon.penup()
enemy = turtle.Turtle()
enemy.penup()
enemy.color("blue")
enemy.goto(random.randint(-200, 200), random.randint(-200, 200))

def player_moves():
    weapon.color("red") 
    weapon.goto(player.position())
    weapon.setheading(player.heading())
    if keyboard.is_pressed("right"):
        player.setheading(0)
        player.forward(10)
    elif keyboard.is_pressed("left"):
        player.setheading(180)
        player.forward(10)
    elif keyboard.is_pressed("up"):
        player.setheading(90)
        player.forward(10)
    elif keyboard.is_pressed("down"):
        player.setheading(270)
        player.forward(10)
    elif keyboard.is_pressed("a"):
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

def enemy_movement():
    enemy_movement_direction = random.choice([1,2,3,4])
    if enemy_movement_direction == 1:
        enemy.setheading(0)
        enemy.forward(10)
    elif enemy_movement_direction == 2:
        enemy.setheading(180)
        enemy.forward(10)
    elif enemy_movement_direction == 3:
        enemy.setheading(90)
        enemy.forward(10)
    elif enemy_movement_direction == 4:
        enemy.setheading(270)
        enemy.forward(10)

screen.setup(width=1.0, height=1.0)
# Register click event handler
while keyboard.is_pressed("esc") == False:
    player_moves()
    enemy_movement()