def turn_right():
    turn_left()
    turn_left()
    turn_left()
   
def left_is_clear():
    turn_left()
    front_is_clear()
    turn_right()

def move_front():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        elif left_is_clear():
            turn_left()
            move_front()
                    
while at_goal()==False:
    move_front()
        

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
