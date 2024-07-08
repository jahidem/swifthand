import random
import sys

# custom modules
from swifthand.helper import Helper
from swifthand.hmac_util import HMACUtill


class Controller:
    def __init__(self, moves):
        self.computer_move = None
        self.moves = moves
        self.rules = None

        self.helper = Helper(moves)
        self.hmac_utils = HMACUtill()
        self.generate_rules()

    def initialize_hmca(self):
        self.hmac_utils.generate_secret_key()
        self.hmac_utils.calculate_hmac(self.computer_move)

    def randomize_computer_move(self):
        self.computer_move = random.choice(
            self.moves
        )  # select a random move from the valid moves

    def generate_rules(self):
        rules = []
        for i, _ in enumerate(self.moves):
            row = []
            for index in range(len(self.moves)):
                if index == i:
                    row.append("Draw")
                elif abs(i - index) <= len(self.moves) / 2:
                    row.append("Win" if index < i else "Lose")
                else:
                    row.append("Win" if index > i else "Lose")
            rules.append(row)
        self.rules = rules

    def prepare_result(self, user_choice):
        result = (
            "You "
            + (self.rules[user_choice][self.moves.index(self.computer_move)])
            + "!"
        )
        print(f"Your move: {self.moves[user_choice]}")
        print(f"Computer move: {self.computer_move}")
        print(result)
        print(f"HMAC key: {self.hmac_utils.secret_key}")
        sys.exit()

    def handle_user_choice(self):
        self.helper.print_menu(self.hmac_utils.curr_hmac)
        choice = input()

        if choice == "0":
            sys.exit()
        elif choice == "?":
            self.helper.rules_table(self.rules)
        elif choice in [str(index) for index in range(1, len(self.moves) + 1)]:
            self.prepare_result(int(choice) - 1)
