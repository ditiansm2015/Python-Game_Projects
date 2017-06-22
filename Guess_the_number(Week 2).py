# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import simplegui



secret_number=0
counter=0

# helper function to start and restart the game
def new_game():	 # initialize global variables used in your code here
   global secret_number
   secret_number=random.randrange(0,100)


# define event handlers for control panel
def range100():
    print "Range is from 0-99"
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    secret_number=random.randrange(0,100)
    global counter
    counter=7
    print "You have",counter,"chances"

def range1000():
    # button that changes the range to [0,1000) and starts a new game 
    print "Range is from 0-999"
    global secret_number
    secret_number=random.randrange(0,1000)
    global counter
    counter=10
    print "You have",counter,"chances"
    
    
def input_guess(guess):
    # main game logic goes here
    global counter
    if counter>0:
        counter=counter-1
        guess_no = int(guess)
        if guess_no==secret_number:
            print "correct guess"
        elif guess_no>secret_number:
           print "Guess was",guess_no
           print "Number of remaining guesses is",counter
           print "Lower"
        else:
            print "Guess was",guess_no
            print "Number of remaining guesses is",counter
            print "Higher"
    
    
    
   

    
# create frame
frame=simplegui.create_frame("Guess The Number",400,400)


# register event handlers for control elements and start frame
frame.add_button("RANGE 0-100",range100)
frame.add_button("Range 0-1000",range1000)
frame.add_input('Your Guess', input_guess, 100)
frame.start()

# call new_game 
new_game()



  


