"""Turtle-based map drawing for the travel adventure."""
from typing import List, Tuple
import math
import turtle

Coordinate = Tuple[str, float, float]


def _project(lat: float, lon: float, radius: float, center_lon: float) -> Tuple[float, float, bool]:
    """Project latitude/longitude using orthographic projection.

    Returns (x, y, visible) where visible tells if the point is on the front-facing
    hemisphere for the given central meridian.
    """

    lat_r = math.radians(lat)
    lon_r = math.radians(lon - center_lon)
    x = radius * math.cos(lat_r) * math.sin(lon_r)
    y = radius * math.sin(lat_r)
    visible = math.cos(lat_r) * math.cos(lon_r) >= 0
    return x, y, visible


def _draw_globe_outline(pen: turtle.Turtle, radius: float, center_lon: float) -> None:
    ocean = turtle.Turtle()
    ocean.hideturtle()
    ocean.penup()
    ocean.color("#0a2342")
    ocean.goto(0, -radius)
    ocean.begin_fill()
    ocean.pendown()
    ocean.circle(radius)
    ocean.end_fill()

    highlight = turtle.Turtle()
    highlight.hideturtle()
    highlight.penup()
    highlight.color("#153b6d")
    highlight.goto(0, -radius + 8)
    highlight.pendown()
    highlight.circle(radius - 8)

    pen.color("#4fa3d1")
    pen.pensize(1)
    pen.penup()

    for lat in (-60, -30, 0, 30, 60):
        lat_r = math.radians(lat)
        y = radius * math.sin(lat_r)
        r = radius * math.cos(lat_r)
        pen.goto(0, y - r)
        pen.pendown()
        pen.circle(r)
        pen.penup()

    for lon_offset in (-120, -60, 0, 60, 120):
        points = []
        lon = center_lon + lon_offset
        for lat in range(-80, 85, 5):
            x, y, visible = _project(lat, lon, radius, center_lon)
            if visible:
                points.append((x, y))
        if not points:
            continue
        pen.goto(points[0])
        pen.pendown()
        for x, y in points[1:]:
            pen.goto(x, y)
        pen.penup()

    pen.color("lightblue")
    pen.pensize(2)
    pen.goto(0, -radius)
    pen.pendown()
    pen.circle(radius)
    pen.penup()


def _draw_route(visits: List[Coordinate], radius: float, center_lon: float) -> None:
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
        x, y, visible = _project(lat, lon, radius, center_lon)
        if not visible:
            continue
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
    center_lon = sum((lon for _, _, lon in visits), 0.0) / len(visits) if visits else -84.5
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)

    _draw_globe_outline(pen, radius, center_lon)
    if visits:
        _draw_route(visits, radius, center_lon)
    _write_summary(visits)

    screen.tracer(True)
    turtle.done()
