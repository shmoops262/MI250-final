"""Interactive choose-your-own-adventure about life after graduation."""
from typing import List, Tuple

from map_visualizer import draw_travel_map
from travel_story import describe_node, get_node, get_start_node_id, record_location

Coordinate = Tuple[str, float, float]


EXIT_WORDS = {"quit", "exit", "done"}


def prompt_choice(option_count: int) -> int | None:
    """Ask the player for a choice and validate it."""
    while True:
        raw = input("Your choice: ").strip().lower()
        if raw in EXIT_WORDS:
            return None
        if raw.isdigit():
            selection = int(raw) - 1
            if 0 <= selection < option_count:
                return selection
        print("Please enter a valid option number or type 'quit' to finish.")


def play_adventure(player_name: str) -> List[Coordinate]:
    """Run the main interactive loop and return visited locations."""
    visited: List[Coordinate] = [("East Lansing, Michigan", 42.73698, -84.48387)]
    current_id = get_start_node_id()

    print(f"\nWelcome, {player_name}! Each choice takes you somewhere new. Type 'quit' anytime to end and draw your map.\n")

    while True:
        node = get_node(current_id)
        print(describe_node(node))
        choice_index = prompt_choice(len(node.options))
        if choice_index is None:
            break

        option = node.options[choice_index]
        location = record_location(option)
        if location:
            visited.append(location)
        current_id = option.next_id

    return visited


def main() -> None:
    name = input("What's your name? ").strip() or "Spartan"
    visits = play_adventure(name)
    print("\nDrawing your travel map... close the Turtle window when you're done reviewing your journey.")
    draw_travel_map(visits)


if __name__ == "__main__":
    main()
