#import turtle
#tim = turtle.Turtle() # ponizej latwiej bo nazwy turtle. nie trzeba powtarzac

# import turtle as t #skraca
import turtle as t
from turtle import Turtle, Screen
import random


tim = Turtle()
tim.shape("turtle")
#tim.color("green")
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]


#directions = [0, 90, 180, 270]
#size = [2, 5, 7, 10, 12, 15]
tim.speed("fastest")

def draw_spirograph(size_of_gaph):
    for i in range(int(360 / size_of_gaph)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gaph)
        ## move circle about +10
        # tim.setheading(tim.heading() + 10) #static



# num_sides = 5 #static

# rysunek!!!
# def draw_shape(num_sides):
#
#     for i in range(num_sides):
#         angle = 360 / num_sides
#         tim.forward(100)
#         tim.right(angle)
#
# for i in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(i)

#drawing with random directions and random pensize
# for i in range(200):
#     tim.color(random_color())
#     tim.pensize(random.choice(size))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))



screen = Screen()
screen.exitonclick()
