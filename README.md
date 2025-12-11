# MI250 Final Project: Post-Grad Travel Adventure

This project is an interactive choose-your-own-adventure about graduating from Michigan State University and deciding what comes next. Players can jump into work at Circa Resort in Las Vegas, head home to Grand Rapids, roam Europe (including a stop at Matka Canyon), or wander the Great Lakes. Every choice records a new destination, and quitting the story draws a Turtle globe that maps everywhere the player traveled.

## To Run

1. Ensure you have Python 3 installed.
2. From the project directory, start the adventure:
   ```bash
   python main.py
   ```
3. Enter your name, then read the narrative text. Type the number next to an option to move to that destination.
4. Type `quit`, `done`, or `exit` at any prompt to finish the story and open a Turtle window that draws your travel map. Close the Turtle window to exit fully.

## Code Overview

- `main.py`: Handles user interaction, input validation, and the main game loop. It records every location visited and triggers the Turtle map when the player chooses to quit.
- `travel_story.py`: Stores the narrative content and decision tree as data classes. Provides helper functions to describe scenes and record location coordinates, keeping story text separate from runtime logic.
- `map_visualizer.py`: Uses the Turtle module to render a globe with latitude/longitude grid lines, draw the player's travel route, and label each visited destination.

## Author Statement

I intentionally separated story content (`travel_story.py`) from the runtime logic (`main.py`) so the narrative can grow without tangling control flow. The Turtle map in `map_visualizer.py` adds a visual finale that reinforces how each programming concept—functions, loops, and modular design—supports the overall story of exploring life after graduation.
