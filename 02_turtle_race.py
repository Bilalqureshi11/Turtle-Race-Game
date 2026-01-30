from turtle import Turtle,Screen
import random

screen = Screen()

is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet',prompt='Which turtle will win the race? enter a color:')

colors = ['red','orange','yellow','green','blue','purple']

all_turtles = []
y_positions = [-70,-40,-10,20,50,80]

for turtle_index in range(0,6):
    tim = Turtle('turtle')
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-240, y=y_positions[turtle_index])
    tim.forward

    all_turtles.append(tim)

print(all_turtles)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(1,10)
        turtle.forward(rand_distance)

        if turtle.xcor() > 230:
            is_race_on = False

            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The winner is {winning_color} turtle")
            else:
                print(f"You've lost! The winner is {winning_color} turtle")

        


screen.exitonclick()

