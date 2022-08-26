# Turtle-Race
Python turtle practice

https://docs.python.org/3/library/turtle.html

https://realpython.com/beginners-guide-python-turtle/#filling-in-an-image

https://docs.python.org/3/library/turtle.html#turtle.shape
***
https://replit.com/@Amun84/turtle2#main.py

https://replit.com/@EssDoe/turtle2#main.py

https://skoolofcode.us/blog/build-turtle-race-game-using-python/

https://trinket.io/python/9339862606

https://pythonguides.com/python-turtle-race/

https://www.futurelearn.com/info/courses/object-oriented-principles/0/steps/31480
***
https://www.geeksforgeeks.org/turtle-addshape-function-in-python/

https://replit.com/talk/ask/Python-Turtle-using-images/8931

https://www.youtube.com/watch?v=SeXgkASIQcA

https://pythonguides.com/python-turtle-size/
***

https://holypython.com/python-turtle-tutorial/turtle-penup-and-pendown/

https://vegibit.com/change-pen-color-in-python-turtle/

https://www.geeksforgeeks.org/how-to-use-images-as-backgrounds-in-tkinter/

##Pseudocode
1. Prep
   1. Create folders with sprites
   2. Create folders with backgrounds
   3. Choose corresponding colors in hexadecimal
      1. for pendown, "yoshi.color" attribute to yoshi object
         1. e.g. pendown(color=yoshi.color)

2. Program
   1. Create gui
      1. choices for basic backgrounds (lambda)
      2. bet on a color (lambda)
         1. Use egg sprites as button visuals
      3. enter username
      4. enter code (optional)
      5. press start!
3. New window open (popup)
4. Begin turtle race
5. Result: Change three winner sprites to G,S,B respectively


###LEVEL UP
1. Add random deterrents (eg. rocks)
   1. If a turtle hits the deterrent, they are out!
2. Add a random enemy (hawk/eagle)
   1. randomly grabs one turtle--even the winners!
      1. if winner is grabbed, turtle #2 becomes de facto winner
3. Scoreboard
   1. Popup window
   2. 5 high scores
      1. use deluxe yoshi sprites for each (R,P,G,S,B)
4. Secrets
   1. Secret codes are shown to a user if:
      1. they win a bet (always)
      2. they end up dead last (random, 8% chance)
      3. they play 3 times in a row (random, 24% chance)
      4. they play 10 times in a row (random, 80% chance)
      5. the user bets (i.e. *any* play--> 0.8% chance)
   2. Enter a secret code to:
      1. bet on a rainbow yoshi--meaning if any yoshi wins, you win!
      2. get 2 bets
      3. add black yoshi to race
      4. add white yoshi to race
      5. add brown yoshi to race
      6. add platinum yoshi ability
         1. slow down a color of your choice at any given time
      7. *control* your color of choice
      8. gain invincibility from deterrents
      9. access secret backgrounds
      10. play against someone else
   3. compound probabilities of these code occurrences
      1. e.g.: rainbow yoshi code has a 0.6% chance of being shown to the player, even if they won their bet
   4. Copy to clipboard button


turtle.isvisible()
turtle.hideturtle()
turtle.ht()