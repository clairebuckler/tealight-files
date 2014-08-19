from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

def go():
  if touch() == 'fruit':
    move()
  elif touch() == 'wall':
    turn(1)
  else 
    move()
    
go()
  
    