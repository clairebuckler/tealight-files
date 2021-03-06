from tealight.logo import move, turn, color

colors = ["red", "green", "blue"]
def square(side):
  for i in range(0,4):
    move(side)
    turn(90)

def triangle(side):
  for i in range (0,3):
    move(side)
    turn(120)
    
def waterwheel(edges, size):
  angle = 360 / edges
  decoration = size / 2
  for i in range(0, edges):
    move(size)
    triangle(decoration)
    turn(angle)
    color(colors[i%3])
    
  

turn(-90)
waterwheel(20,50)
