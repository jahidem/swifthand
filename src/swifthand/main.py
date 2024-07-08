import sys

# custom modules
from swifthand.controller import Controller


valid_moves = sys.argv[1:]
controller = Controller(valid_moves)


def run():
    controller.randomize_computer_move()
    controller.initialize_hmca()
    while True:
        controller.handle_user_choice()


if __name__ == "__main__":
    run()
