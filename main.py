from turtle import Screen
import turtle as t
import random

# import heroes
# print(heroes.gen())

tim = t.Turtle()
t.colormode(255)

tim.shape("turtle")
tim.color("red")


# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.left(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shapes(shape_side_n)

# directions = [0, 90, 180, 270]
# tim.pensize(15)

# for step in range(200):
#     tim.color((random_color()))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)
    return color

tim.speed("fastest")

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)








screen = Screen()
screen.exitonclick()
