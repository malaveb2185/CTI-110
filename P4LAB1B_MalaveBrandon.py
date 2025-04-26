#Brandon Malave 
# 04/26/2025
#P4LAB1B
#Use turtle to draw initials B and M

import turtle 

#Create window and turtle 
win = turtle.Screen()
pen = turtle.Turtle()

#Turtle settings 
pen.pensize(5)
pen.pencolor("blue")
pen.shape("arrow")

#Draw B 
pen.left(90)
pen.forward(100)
pen.right(90)
pen.circle(-25, 180)
pen.right(180)
pen.circle(-25, 180)

#Move to draaw M
pen.penup()
pen.right(90)
pen.forward(100)
pen.pendown()

#Draw M 
pen.left(90)
pen.forward(100)
pen.right(135)
pen.forward(70)
pen.left(90)
pen.forward(70)
pen.right(135)
pen.forward(100)


#Wait for user to close window 
win.mainloop()