def is_dirty(environment, room):
    """Return True when the selected room is dirty."""
    return environment[room] == "Dirty"

def clean_room(environment, room):
    """Change the selected room's state to Clean."""
    environment[room] = "Clean"

class VacuumAgent:
    """Rule-based agent that operates in rooms A and B."""

    def __init__(self, environment, starting_room="A"):
        self.environment = environment
        self.current_room = starting_room

    def move(self):
        """Move to the other room."""
        self.current_room = "B" if self.current_room == "A" else "A"

    def perceive_and_act(self):
        """Agents Rules

        Rule 1: If the current room is dirty, clean it.
        Rule 2: If the current room is clean, move to the other room.
        """
        if is_dirty(self.environment, self.current_room):
            clean_room(self.environment, self.current_room)
            return f"Cleaned room {self.current_room}."

        previous_room = self.current_room
        self.move()
        return f"Moved from room {previous_room} to room {self.current_room}."

def read_room_state(room):
    """Validate initial state"""
    while True:
        state = input(f"Enter the initial state of room {room} (dirty/clean): ").strip().lower()
        if state in {"dirty", "clean"}:
            return state.capitalize()
        print("Invalid input. Please enter dirty or clean.")

def read_step_count():
    """Validate simulation of steps"""
    while True:
        try:
            steps = int(input("How many simulation steps should run? ").strip())
            if steps >= 1:
                return steps
        except ValueError:
            pass
        print("Invalid input. Enter a whole number greater than or equal to 1.")

def format_environment(environment):
    """Return to readable form"""
    return f"A={environment['A']}, B={environment['B']}"

def main():
    """Simulation and Display"""
    print("Rule-Based Vacuum Cleaner Agent")
    print("--------------------------------")

    # The environment is represented by a dictionary with two rooms.
    environment = {
        "A": read_room_state("A"),
        "B": read_room_state("B"),
    }
    steps = read_step_count()
    agent = VacuumAgent(environment)

    print(f"\nInitial environment: {format_environment(environment)}")
    print(f"Starting location: room {agent.current_room}")

    for step in range(1, steps + 1):
        action = agent.perceive_and_act()
        print(f"\nStep {step}")
        print(f"Current location: room {agent.current_room}")
        print(f"Action taken: {action}")
        print(f"Environment: {format_environment(environment)}")

    print("\nSimulation complete.")

if __name__ == "__main__":
    main()
