import turtle
import random

timmy = turtle.Turtle()
timmy.shape("turtle")
turtle.colormode(255)

# for x in range(4):
#     timmy.forward(100)
#     timmy.right(90)


# for x in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


# def calc(sides):
#     for x in range(sides):
#         timmy.forward(100)
#         timmy.right(360/sides)
#
# for x in range(3, 11):
#     calc(x)
#     timmy.color(random.random(), random.random(), random.random())

# random direction

def random_turn():
    degree = [0, 90, 180, 270]
    choice = random.choice(degree)
    timmy.setheading(choice)


def color_change():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# for x in range(100):
#     timmy.color(color_change())
#     timmy.speed(8)
#     timmy.pensize(10)
#     random_turn()
#     timmy.forward(30)


def spirograph(degree):
    new_degree = 0
    for x in range(int(360/degree)):
        timmy.color(color_change())
        timmy.speed(10)
        timmy.pensize(1)
        timmy.circle(75)
        new_degree += degree
        timmy.setheading(new_degree)


spirograph(10)

screen = turtle.Screen()
screen.exitonclick()