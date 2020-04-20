#Football game
import turtle
import os
import math
import time

#Set up the screen
wn=turtle.Screen()
wn.bgcolor("skyblue")
turtle.register_shape("ball.gif")
turtle.register_shape("player.gif")
turtle.register_shape("receiver.gif")

def make_area():
    #Draw grass
    grass = turtle.Turtle()
    grass.color("green")
    grass.shape("square")
    grass.shapesize(20,200)
    grass.penup()
    grass.setposition(-170,-180)

    #draw grass lines
    for i in range(5):
        angle = -30
        x_pos = -225
        line = turtle.Turtle()
        line.color("white")
        line.shape("square")
        line.shapesize(23,.25)
        line.penup()
        line.tilt(angle+(i*15))
        line.setposition(x_pos+(i*125),-225)
    
def player (color,position="QB"):
    #Create the player
    player_x = turtle.Turtle()
    if position == "QB":
        player_x.shape("player.gif")
        player_x.color(color)
        player_x.penup()
        player_x.setposition(-190,-130)
    else:
        player_x.shape("receiver.gif")
        player_x.color(color)
        player_x.penup()
        player_x.setposition(160,-130)




make_area()            
qb_player = player("red")
r_player = player("blue","r")

#Create the football
football = turtle.Turtle()
football.shape("ball.gif")
football.shapesize(1,1)
football.penup()
football.setposition(-155,-130)



#Throwing the ball
def toss():
  #user inputs the angle
    if football.xcor() < 0:
        velocity  = 4
        v = (50 + velocity)
        football.penup()
        football.setposition(-150,-150)
        football.pendown()
        for t in range(0,12):
            x = -150 + v/2 * t
            y = -150 + v * t - 9.8 / 2 * t**2
            football.penup()
            football.goto(x, y)
    else:
        velocity  = 4
        v = (50 + velocity)
        for t in range(0,12):
            x = 150 - v/2 * t
            y = -150 + v * t - 9.8 / 2 * t**2
            football.penup()
            football.goto(x, y)


turtle.listen()
turtle.onkey(toss,"Up")

  

 
       
