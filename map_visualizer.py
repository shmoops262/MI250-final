"""Turtle-based map drawing for the travel adventure."""
from typing import Iterable, List, Tuple
import turtle

Coordinate = Tuple[str, float, float]


def _draw_ocean(bounds: Tuple[float, float, float, float]) -> None:
    ocean = turtle.Turtle(visible=False)
    ocean.speed(0)
    ocean.penup()
    ocean.color("#06243d")
    west, south, east, north = bounds
    ocean.goto(west, south)
    ocean.begin_fill()
    ocean.pendown()
    for point in [(west, north), (east, north), (east, south), (west, south)]:
        ocean.goto(point)
    ocean.end_fill()
    ocean.penup()


def _draw_graticule(bounds: Tuple[float, float, float, float]) -> None:
    grid = turtle.Turtle(visible=False)
    grid.speed(0)
    grid.color("#1d4f7a")
    grid.pensize(1)
    west, south, east, north = bounds

    for lon in range(-180, 181, 30):
        grid.penup()
        grid.goto(lon, south)
        grid.pendown()
        grid.goto(lon, north)

    for lat in range(-90, 91, 30):
        grid.penup()
        grid.goto(west, lat)
        grid.pendown()
        grid.goto(east, lat)


def _draw_continent(outline: Iterable[Tuple[float, float]], fill: str) -> None:
    pen = turtle.Turtle(visible=False)
    pen.speed(0)
    pen.color(fill)
    pen.penup()
    points = list(outline)
    if not points:
        return
    pen.goto(points[0])
    pen.begin_fill()
    pen.pendown()
    for point in points[1:]:
        pen.goto(point)
    pen.end_fill()


def _draw_landmasses() -> None:
    """Draw simple, recognizable continent silhouettes in lat/lon space."""
    # These polygons are intentionally coarse; they are meant to anchor the map visually
    # rather than replicate detailed geography.
    north_america = [
        (-170, 70), (-140, 72), (-125, 70), (-110, 60), (-102, 50), (-95, 48),
        (-85, 50), (-75, 45), (-80, 35), (-90, 30), (-95, 20), (-100, 15),
        (-110, 20), (-120, 25), (-130, 35), (-140, 50), (-155, 60), (-170, 70)
    ]
    south_america = [
        (-80, 12), (-70, 10), (-65, 0), (-60, -10), (-60, -20), (-62, -30),
        (-70, -40), (-78, -50), (-75, -55), (-70, -52), (-65, -48), (-60, -40),
        (-58, -30), (-58, -20), (-60, -10), (-65, 0), (-70, 8), (-80, 12)
    ]
    africa = [
        (-17, 37), (0, 37), (20, 32), (30, 25), (35, 10), (40, -5), (45, -15),
        (40, -25), (30, -35), (15, -35), (5, -30), (0, -25), (-5, -5),
        (-10, 0), (-15, 10), (-17, 20), (-17, 37)
    ]
    eurasia = [
        (-10, 70), (10, 72), (30, 70), (50, 65), (70, 60), (90, 55), (110, 60),
        (130, 55), (150, 60), (160, 55), (160, 40), (150, 35), (140, 30), (120, 25),
        (100, 20), (80, 15), (60, 20), (40, 25), (30, 30), (20, 40), (10, 45),
        (0, 50), (-10, 55), (-10, 60), (-10, 70)
    ]
    australia = [
        (110, -10), (120, -15), (135, -20), (145, -25), (150, -32), (145, -38),
        (130, -40), (120, -35), (110, -30), (105, -20), (110, -10)
    ]
    greenland = [(-60, 82), (-40, 80), (-20, 75), (-20, 65), (-45, 60), (-60, 65), (-60, 82)]
    india = [(70, 22), (80, 28), (90, 22), (85, 10), (75, 5), (70, 15), (70, 22)]
    antarctica = [
        (-180, -70), (-120, -72), (-60, -74), (0, -76), (60, -74), (120, -72), (180, -70),
        (180, -80), (-180, -80), (-180, -70)
    ]

    for land in [north_america, south_america, africa, eurasia, australia, greenland, india, antarctica]:
        _draw_continent(land, "#4fa35f")


def _draw_route(visits: List[Coordinate]) -> None:
    path = turtle.Turtle(visible=False)
    path.speed(0)
    path.color("gold")
    path.pensize(2)
    path.penup()

    marker = turtle.Turtle(visible=False)
    marker.speed(0)
    marker.color("#f4e409")
    marker.penup()

    previous = None
    for name, lat, lon in visits:
        if previous is None:
            path.goto(lon, lat)
            path.pendown()
        else:
            path.goto(lon, lat)
        marker.goto(lon, lat)
        marker.dot(8, "#f4e409")
        marker.write(name, align="left", font=("Arial", 10, "normal"))
        previous = (lon, lat)


def _write_summary(visits: List[Coordinate], bounds: Tuple[float, float, float, float]) -> None:
    west, south, east, north = bounds
    label = turtle.Turtle(visible=False)
    label.color("white")
    label.penup()
    label.goto((west + east) / 2, north - 10)
    if visits:
        locations = ", ".join(name for name, _, _ in visits)
        label.write(f"You traveled to: {locations}", align="center", font=("Arial", 12, "bold"))
    else:
        label.write("You stayed in East Lansing this time.", align="center", font=("Arial", 12, "bold"))


def draw_travel_map(visits: List[Coordinate]) -> None:
    """Render a flat world map with the player's travel path."""
    screen = turtle.Screen()
    screen.setup(width=1000, height=600)
    screen.title("Your Post-Grad Travel Map")
    screen.bgcolor("black")

    # Use geographic coordinates directly so longitude runs horizontally and latitude vertically.
    bounds = (-190.0, -110.0, 190.0, 110.0)
    screen.setworldcoordinates(*bounds)
    screen.tracer(False)

    _draw_ocean(bounds)
    _draw_graticule(bounds)
    _draw_landmasses()
    if visits:
        _draw_route(visits)
    _write_summary(visits, bounds)

    screen.tracer(True)
    turtle.done()
