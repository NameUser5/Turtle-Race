from turtle import *
from turtle import Turtle
import random

## Turtle screen:
screen = Screen()
screen.setup(width=500, height=400)
screen.screensize(500, 400)

screen.bgcolor('light gray')
screen.bgpic(r'')
screen.title('Turtle Race!')

colors = ['green', 'red', 'blue', 'orange', 'pink', 'cyan', 'purple', 'yellow', 'brown', 'white', 'black']

## YOSHIS ##
platinum_yoshi = r'deluxe yoshis/platinum yoshi.gif'
platinum_yoshi.subsample(9, 9)
screen.register_shape(r'yoshis/black yoshi.gif')
screen.register_shape(r'yoshis/white yoshi.gif')
screen.register_shape(r'yoshis/brown yoshi.gif')
screen.register_shape(r'yoshis/green yoshi.gif')
screen.register_shape(r'yoshis/red yoshi.gif')
screen.register_shape(r'yoshis/blue yoshi.gif')
screen.register_shape(r'yoshis/orange yoshi.gif')
screen.register_shape(r'yoshis/pink yoshi.gif')
screen.register_shape(r'yoshis/cyan yoshi.gif')
screen.register_shape(r'yoshis/purple yoshi.gif')
screen.register_shape(r'yoshis/yellow yoshi.gif')
screen.register_shape(r'deluxe yoshis/bronze yoshi.gif')
screen.register_shape(r'deluxe yoshis/silver yoshi.gif')
screen.register_shape(r'deluxe yoshis/gold yoshi.gif')
screen.register_shape(platinum_yoshi)
screen.register_shape(r'deluxe yoshis/rainbow yoshi.gif')


green_bet = "green"
red_bet = "red"
blue_bet = "blue"
orange_bet = "orange"
pink_bet = "pink"
cyan_bet = "cyan"
purple_bet = "purple"
yellow_bet = "yellow"
brown_bet = "brown"
white_bet = "white"
black_bet = "black"

available_bets = [green_bet, red_bet, blue_bet, orange_bet, pink_bet, cyan_bet, purple_bet, yellow_bet]

hidden_bets = [brown_bet, white_bet, black_bet]

racers = []
bet_options = []

y_axis = 100

random.shuffle(available_bets)

def racer_colors(available_bets):
    global y_axis
    color_names = random.sample(available_bets, 4)
    bet_options.append(color_names)
    idx = 0       # HERE, NOT IN THE LOOP, IS WHAT WAS MISSING!

    for _ in range(4):
        new_turtle = Turtle(shape='turtle')
        new_turtle.penup()

        new_turtle.color(color_names[idx])
        new_turtle.goto(-200, y=y_axis)
        racers.append(new_turtle)
        y_axis -= 50
        idx += 1


racer_colors(available_bets)

user_bet = screen.textinput(title="Bet!", prompt=f"Who will win?\n{bet_options}")


speed(0)
penup()
goto(-180, 120)


# ## Field markings:
for _ in range(11):
    write(_, align='center')
    right(90)
    for _ in range(8):
        penup()
        forward(11)
        pendown()
        forward(11)
    penup()
    backward(176)
    left(90)
    forward(30)

write("Finish!", align="center")
color('Red')
right(90)
forward(10)
pendown()
forward(174)
penup()


def display_winner(winner):
    print(f"The {winner} turtle is the winner!\n...but you get nothing in return. Sorry!")
    announcer_turtle.showturtle()
    announcer_turtle.write(f"The {winner} turtle is the winner!\n...but you get nothing in return. Sorry!      ", True)
    done()

game_run = ''
announcer_turtle = Turtle(shape='turtle')
announcer_turtle.hideturtle()
announcer_turtle.color('gray')
announcer_turtle.shape(platinum_yoshi)
announcer_turtle.pencolor('black')
announcer_turtle.penup()
announcer_turtle.goto(-190, -100)
announcer_turtle.hideturtle()

if user_bet:
    game_run = True

while game_run:
    for _ in racers:
        _.forward(random.randint(0, 10))
        if _.xcor() >= 150:
            race_on = False
            winner = _.pencolor()
            if winner == user_bet.lower():
                display_winner(winner)
            else:
                announcer_turtle.showturtle()
                announcer_turtle.write(f"You bet on {user_bet}.\nThe {winner} turtle won. Sorry.      ", True)
                print(f"You bet on {user_bet}.\nThe {winner} turtle won. Sorry.")
                done()


done()

# turtle.exitonclick()
