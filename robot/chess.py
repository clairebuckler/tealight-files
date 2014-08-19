from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

def go():
  moved = 0
  if touch() == 'fruit':
    move()
    moved = moved + 1
  elif touch() == None:
    turn(1)
  else:
    turn(1)
    go()
    
  for i in range(0,moved):
    go()
    
    
go()
  
    