from turtle import *
from turtle import Turtle
import random
import time

## Turtle screen:
screen = Screen()
screen.setup(width=500, height=400)
screen.screensize(500, 400)

screen.bgcolor('black')
screen.bgpic(r'')
screen.title('Yoshi Race!')

# colors = ['green', 'red', 'blue', 'orange', 'pink', 'cyan', 'purple', 'yellow', 'brown', 'white', 'black']

## YOSHIS ##
rainbow_yoshi = r'deluxe yoshis/rainbow yoshi.gif'
platinum_yoshi = r'deluxe yoshis/platinum yoshi.gif'
gold_yoshi = r'deluxe yoshis/gold yoshi.gif'
silver_yoshi = r'deluxe yoshis/silver yoshi.gif'
bronze_yoshi = r'deluxe yoshis/bronze yoshi.gif'
black_yoshi = r'yoshis/black yoshi.gif'
brown_yoshi = r'yoshis/brown yoshi.gif'
white_yoshi = r'yoshis/white yoshi.gif'
green_yoshi = r'yoshis/green yoshi.gif'
red_yoshi = r'yoshis/red yoshi.gif'
orange_yoshi = r'yoshis/orange yoshi.gif'
yellow_yoshi = r'yoshis/yellow yoshi.gif'
blue_yoshi = r'yoshis/blue yoshi.gif'
cyan_yoshi = r'yoshis/cyan yoshi.gif'
purple_yoshi = r'yoshis/purple yoshi.gif'
pink_yoshi = r'yoshis/pink yoshi.gif'

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

game_flag = True
while game_flag == True:
    screen.register_shape(rainbow_yoshi)
    screen.register_shape(platinum_yoshi)
    screen.register_shape(gold_yoshi)
    screen.register_shape(silver_yoshi)
    screen.register_shape(bronze_yoshi)
    screen.register_shape(black_yoshi)
    screen.register_shape(brown_yoshi)
    screen.register_shape(white_yoshi)
    screen.register_shape(green_yoshi)
    screen.register_shape(red_yoshi)
    screen.register_shape(orange_yoshi)
    screen.register_shape(yellow_yoshi)
    screen.register_shape(blue_yoshi)
    screen.register_shape(cyan_yoshi)
    screen.register_shape(purple_yoshi)
    screen.register_shape(pink_yoshi)

    def reset_all(turtle):
        turtle.reset()
        screen.reset()

    available_bets = ['green', 'red', 'blue', 'orange', 'pink', 'cyan', 'purple', 'yellow']

    hidden_bets = ['brown', 'white', 'black']

    secret_codes = []

    racers = []
    bet_options = []

    y_axis = 100

    random.shuffle(available_bets)

    ## SET YOSHI POSITIONS:
    def racer_colors(available_bets):
        global y_axis
        color_names = random.sample(available_bets, 4)
        bet_options.append(color_names)
        idx = 0  # HERE, NOT IN THE LOOP, IS WHAT WAS MISSING!

        for _ in range(4):
            new_turtle = Turtle(shape='turtle')
            new_turtle.penup()

            new_turtle.color(color_names[idx])
            determine_image(new_turtle, color_names[idx])
            screen.listen()

            new_turtle.goto(-200, y=y_axis)
            racers.append(new_turtle)
            print(new_turtle.pos())
            y_axis -= 50
            idx += 1


    def determine_image(turtle, color):
        if color == 'green':
            return turtle.shape(green_yoshi)
        elif color == 'red':
            return turtle.shape(red_yoshi)
        elif color == 'orange':
            return turtle.shape(orange_yoshi)
        elif color == 'yellow':
            return turtle.shape(yellow_yoshi)
        elif color == 'blue':
            return turtle.shape(blue_yoshi)
        elif color == 'cyan':
            return turtle.shape(cyan_yoshi)
        elif color == 'purple':
            return turtle.shape(purple_yoshi)
        elif color == 'pink':
            return turtle.shape(pink_yoshi)
        elif color == 'white':
            return turtle.shape(white_yoshi)
        elif color == 'brown':
            return turtle.shape(brown_yoshi)
        elif color == 'black':
            return turtle.shape(black_yoshi)

        #     ## UMPIRE (UPDATES TO USER)
        # announcer_turtle = Turtle(shape='turtle')
        # announcer_turtle.hideturtle()
        # announcer_turtle.color('gray')
        # announcer_turtle.shape(platinum_yoshi)
        #
        # announcer_turtle.pencolor('light gray')
        # announcer_turtle.penup()
        # announcer_turtle.goto(-190, -115)
        # announcer_turtle.hideturtle()
        #
        # screen.listen()
        # else:
        #     return turtle.shape(black_yoshi)          # wasn't working (why though???)
        screen.listen()


    racer_colors(available_bets)

    user_bet = screen.textinput(title="Bet!", prompt=f"Who will win?\n{bet_options}").lower()
    # def validate_bet(bet, options, codes):
    #         if bet in options:
    #             return bet
    #         else:
    #             flag = True
    #             while flag:
    #                 if bet not in codes:
    #                     user_bet = screen.textinput(title="Bet!", prompt=f"Who will win?\n{bet_options}").lower()

    # validate_bet(user_bet, bet_options, secret_codes)

    speed(0)
    penup()
    goto(-180, 120)

    ## Field markings:
    for _ in range(11):
        write(_, align='center')
        color('light gray')
        right(90)
        for _ in range(8):
            penup()
            forward(12)
            pendown()
            forward(12)
        penup()
        backward(192)
        left(90)
        forward(30)

    write("Finish!", align="center")
    color('Red')
    right(90)
    forward(10)
    pendown()
    forward(190)  # put 2 less than line 144
    penup()

    ## PROMPTS THE UMPIRE TO DECLARE THE WINNER
    def display_winner(winner):
        print(f"The {winner} yoshi is the winner!\n...but you get nothing in return. Sorry!")
        announcer_turtle.showturtle()
        announcer_turtle.write(f"The {winner} yoshi is the winner!\n...but you get nothing in return. Sorry!     ", True)
        play_again()
        # resetscreen()
        done()

    def play_again():
        time.sleep(3)
        confirm_replay = screen.textinput(title="Play again?", prompt=f"Press [OK] to play again. Enter a secret code if you "
                                                              f"have one.").upper()
        if confirm_replay == '':
            screen.resetscreen()

            # for _ in racers:
            #     _.reset()

            racers = []

            announcer_turtle.reset()
            announcer_turtle.hideturtle()
            announcer_turtle.color('gray')
            announcer_turtle.shape(platinum_yoshi)

            announcer_turtle.pencolor('light gray')
            announcer_turtle.penup()
            announcer_turtle.goto(-190, -115)
            announcer_turtle.hideturtle()

            screen.listen()
            game_flag = True
        else:
            game_flag = False

    ## UMPIRE (UPDATES TO USER)
    announcer_turtle = Turtle(shape='turtle')
    announcer_turtle.hideturtle()
    announcer_turtle.color('gray')
    announcer_turtle.shape(platinum_yoshi)

    announcer_turtle.pencolor('light gray')
    announcer_turtle.penup()
    announcer_turtle.goto(-190, -115)
    announcer_turtle.hideturtle()

    screen.listen()

    ## PROMPT RACE
    game_run = ''
    if user_bet:
        game_run = True

    ## CODE FOR RACERS
    while game_run:
        for _ in racers:
            _.forward(random.randint(0, 10))
            if _.xcor() >= 150:
                game_run = False
                winner = _.pencolor()
                if winner == user_bet.lower():
                    display_winner(winner)
                    play_again()
                else:
                    announcer_turtle.showturtle()
                    announcer_turtle.write(f"You bet on {user_bet}.\nThe {winner} yoshi won. Sorry.      ", True)
                    print(f"You bet on {user_bet}.\nThe {winner} yoshi won. Sorry.")
                    play_again()
                    # resetscreen()
                    # announcer_turtle.resetscreen()
                    # done()
                    mainloop()


    screen.mainloop()
