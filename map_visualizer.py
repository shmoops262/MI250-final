"""Turtle-based map drawing for the travel adventure."""
from typing import List, Tuple
import turtle

Coordinate = Tuple[str, float, float]


def _project(lat: float, lon: float, radius: float) -> Tuple[float, float]:
    """Project latitude/longitude onto a simple circular map."""
    x = (lon / 180) * radius
    y = (lat / 90) * radius
    return x, y


def _draw_globe_outline(pen: turtle.Turtle, radius: float) -> None:
    pen.color("lightblue")
    pen.pensize(2)
    pen.penup()
    pen.sety(-radius)
    pen.pendown()
    pen.circle(radius)

    pen.penup()
    pen.color("#4fa3d1")
    for lat in (-60, -30, 0, 30, 60):
        y = (lat / 90) * radius
        pen.goto(-radius, y)
        pen.pendown()
        pen.forward(2 * radius)
        pen.penup()

    pen.setheading(90)
    for lon in (-120, -60, 0, 60, 120):
        pen.goto((lon / 180) * radius, -radius)
        pen.pendown()
        pen.forward(2 * radius)
        pen.penup()
    pen.setheading(0)


def _draw_route(visits: List[Coordinate], radius: float) -> None:
    path = turtle.Turtle()
    path.hideturtle()
    path.speed(0)
    path.color("gold")
    path.pensize(2)
    path.penup()

    marker = turtle.Turtle()
    marker.hideturtle()
    marker.speed(0)
    marker.color("#f4e409")
    marker.penup()

    previous = None
    for name, lat, lon in visits:
        x, y = _project(lat, lon, radius)
        if previous is None:
            path.goto(x, y)
            path.pendown()
        else:
            path.goto(x, y)
        marker.goto(x, y)
        marker.dot(10, "#f4e409")
        marker.write(name, align="left", font=("Arial", 10, "normal"))
        previous = (x, y)


def _write_summary(visits: List[Coordinate]) -> None:
    label = turtle.Turtle()
    label.hideturtle()
    label.color("white")
    label.penup()
    label.goto(0, 260)
    if visits:
        locations = ", ".join(name for name, _, _ in visits)
        label.write(f"You traveled to: {locations}", align="center", font=("Arial", 12, "bold"))
    else:
        label.write("You stayed in East Lansing this time.", align="center", font=("Arial", 12, "bold"))


def draw_travel_map(visits: List[Coordinate]) -> None:
    """Render a globe with the player's travel path."""
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Your Post-Grad Travel Map")
    screen.bgcolor("midnight blue")
    screen.tracer(False)

    radius = 280
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)

    _draw_globe_outline(pen, radius)
    if visits:
        _draw_route(visits, radius)
    _write_summary(visits)

    screen.tracer(True)
    turtle.done()
