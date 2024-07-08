import sys
from prettytable import PrettyTable


class Helper:
    """
    This class provides functions to help printing ASCII instructions on terminal
    """

    def __init__(self, moves) -> None:
        self.moves = moves

    def validate_moves(self):
        has_duplicates = len(self.moves) != len(set(self.moves))

        if len(self.moves) < 3:
            print("Error: You must provide three or more odd number of moves.")
        elif len(self.moves) % 2 == 0:
            print("Error: You must provide odd number of moves.")
        elif has_duplicates:
            print("Error: You  must provide uniques names for the moves")
        else:
            return
        print("Example of valid move initialization: Rock Paper Scissors Lizard Spock")
        sys.exit()

    def rules_table(self, rules):
        table = PrettyTable()
        table.field_names = ["MOVES ↓→"] + self.moves
        for row, move in zip(rules, self.moves):
            table.add_row([move] + row, divider=True)

        print(table)

    def print_menu(self, curr_hmac):
        ui_moves = "\n".join([f"{i+1} - {item}" for i, item in enumerate(self.moves)])
        print(f"HMAC: {curr_hmac}\nAvailable moves:")
        print(
            ui_moves,
            "\n0 - exit\n? - help\nEnter your move:",
            end="",
        )
