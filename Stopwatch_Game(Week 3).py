# template for "Stopwatch: The Game"
import simplegui

# define global variables
minute=0
sec=0
millisec=0
interval=100
watch=0
stopwatch=""


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global millisec,sec,minute,stopwatch
    millisec=t%10;
    t=t/10;
    sec=t%60
    t=t/60
    minute=t%60
    if sec<10:
        sec="0"+str(sec)
    stopwatch=str(minute)+":"+str(sec)+"."+str(millisec)
    
        
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():  
    timer.start()
    
    
def Stop():
    timer.stop()
    
    
def Reset():
    global minute,sec,millisec,watch
    timer.stop()
    watch=0
    frame.set_draw_handler(draw)
    format(watch)




# define event handler for timer with 0.1 sec interval
def update():
    global watch
    watch=watch+1
    format(watch)


# define draw handler
def draw(canvas):
    global stopwatch
    canvas.draw_text((stopwatch),(150,250),40,"White")

    
# create frame
frame=simplegui.create_frame("STOPWATCH GAME",500,500)
frame.add_button("Start",Start)
frame.add_button("Stop",Stop)
frame.add_button("Reset",Reset)
frame.set_draw_handler(draw)

#create timer
timer=simplegui.create_timer(interval,update)



# register event handlers


# start frame
frame.start()
                             


# Please remember to review the grading rubric
