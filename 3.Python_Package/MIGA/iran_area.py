import turtle
import requests


def main():
    # Get data
    url = "https://raw.githubusercontent.com/johan/world.geo.json/master/countries/IRN.geo.json"
    data = requests.get(url).json()

    coordinates = data["features"][0]["geometry"]["coordinates"][0]

    screen = turtle.Screen()
    screen.title("Iran")
    screen.setup(width=1400, height=950)
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.pensize(2)
    t.color("black", "#f4d27a") 

    scale = 24  
    offset_x, offset_y = 55, 32

    t.penup()
    t.begin_fill()

    for lon, lat in coordinates:
        x = (lon - offset_x) * scale
        y = (lat - offset_y) * scale
        t.goto(x, y)
        t.pendown()

    t.end_fill()

    t.penup()
    t.color("darkred")
    t.goto(0, 150)
    t.write("IRAN", align="center", font=("Arial", 32, "bold"))

    t.goto(0, -420)
    t.color("black")
    t.write("", align="center", font=("Arial", 14, "normal"))

    screen.exitonclick()
