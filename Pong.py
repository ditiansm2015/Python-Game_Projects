# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle1_pos=[PAD_WIDTH,PAD_HEIGHT]
paddle2_pos=[WIDTH-BALL_RADIUS,PAD_HEIGHT]

ball_pos=[WIDTH/2,HEIGHT/2]
ball_vel=[0,8]
paddle1_vel=[0,5]
paddle2_vel=[0,5]




# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel, WIDTH, HEIGHT# these are vectors stored as lists
    ball_pos=[WIDTH/2,HEIGHT/2]


# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball("right")
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    paddle1_pos[1]+=paddle1_vel[1]
    paddle1_pos[0]+=paddle1_pos[0]
    
 
   
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    

    # update ball
        
        
        
    # draw ball
    canvas.draw_circle(ball_pos,BALL_RADIUS,2,"White")
        
        
    # update paddle's vertical position, keep paddle on the screen
    
    
    # draw paddles
    canvas.draw_line([paddle1_pos[1],HEIGHT/4],[paddle1_pos[1],HEIGHT/4],16,"White")
    canvas.draw_line([WIDTH , 0],[WIDTH, HEIGHT/4], 16, "White")
    
    # determine whether paddle and ball collide    
    
    # draw scores
        
def keydown(key):
    stopper=1
    if key == simplegui.KEY_MAP['down']:
        paddle1_vel[1]+=stopper   
    
def keyup(key):
    stopper=1
    if key == simplegui.KEY_MAP['up']:
        paddle1_vel[1]-=stopper
              
   

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
