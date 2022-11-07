#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
k=""
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
try:
  wn.addshape(apple_image) # Make the screen aware of the new file 
except: 
  print("Image not found!")
  

apple = trtl.Turtle()
letter = trtl.Turtle()
letter.penup()
letter.hideturtle()
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def reset():
def draw_apple(active_apple):
  active_apple.penup()
  try:
    active_apple.shape(apple_image)
    letter.goto(active_apple.xcor()-13,active_apple.ycor()-30)
    letter.color("white")
    k=key()
    letter.write(k, font=("Arial", 30, "bold"))
  except:
    print("No image!")
  wn.update()
  
def draw_an_A():
  letter.clear()
  apple.goto(apple.xcor(), -175)
  apple.hideturtle()
  wn.update()
  reset()
  draw_apple(apple)

wn.onkeypress(draw_an_A, k)

wn.listen()
def key():
  x=[]
  for i in range(65,91):x.append(chr(i))
  return x.pop(rand.randint(0,len(x)))
#-----function calls-----
draw_apple(apple)
wn.bgpic("background.gif")
wn.mainloop()