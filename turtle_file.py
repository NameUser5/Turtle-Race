from turtle import *
import turtle
import random

## Turtle screen:
screen = Screen()
screen.setup(width=500, height=500)
screen.screensize(500, 500)

screen.bgcolor('light gray')
screen.bgpic(r'')
screen.title('Turtle Race!')

colors = ['green', 'red', 'blue', 'orange', 'pink', 'cyan', 'purple', 'yellow', 'brown', 'white', 'black']

green_bet = "G - Green yoshi"
red_bet = "R - Red yoshi"
blue_bet = "B - Blue yoshi"
orange_bet = "O - Orange yoshi"
pink_bet = "K - Pink yoshi"
cyan_bet = "C - Cyan yoshi"
purple_bet = "P - Purple yoshi"
yellow_bet = "Y - Yellow yoshi"
brown_bet = "W - Brown yoshi"
white_bet = "H - White yoshi"
black_bet = "A - Black yoshi"

available_bets = [green_bet, red_bet, blue_bet, orange_bet]

hidden_bets = [pink_bet, cyan_bet, purple_bet, yellow_bet, brown_bet, white_bet, black_bet]

user_bet = screen.textinput(title="Bet!", prompt=f"Who will win?\n{available_bets} ").upper()

# speed(0)
# penup()
# goto(-140, 140)
#
# ## Field markings:
# for _ in range(11):
#     write(_, align='center')
#     right(90)
#     for _ in range(8):
#         penup()
#         forward(10)
#         pendown()
#         forward(10)
#     penup()
#     backward(160)
#     left(90)
#     forward(20)
#
# class Athlete:
#     def __init__(self, color, position):
#         self.color = color
#         self.position = position

turtle.done()

# green = #44D311
# red = '#EF0000'
# blue = '#2742FF'
# yellow = '#FED905'
# pink = '#FF77BA'
# cyan = '#15D5FD'
# orange = '#FD6907'
# purple = '#8A3DBE'
# black = '#333333'
# white = '#C1D0D0'
# brown = '#AB6021'

# green_yoshi = r'yoshis\green yoshi.png'
# screen = turtle.Screen()
# # image = green_yoshi
# #'yoshis\green yoshi.png'
# screen.addshape(green_yoshi, shape=None)
# turtle.shape(green_yoshi)
#
# # turtle.color('white')
# # turtle.register_shape(r'yoshis\green yoshi.png')
#
# print(turtle.getshapes())

help(register_shape)
# turtle.exitonclick()
