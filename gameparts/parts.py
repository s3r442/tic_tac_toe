class PlayGround:
    """Класс, который описывает игровое поле."""

    side_size = 3

    def __init__(self):
        self.board = [
            ["       " for _ in range(3)] for _ in range(3)
            ]

    def make_move(self, row, col, char):
        self.board[row][col] = "   " + char + "   "

    def display(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 23)

    def __str__(self):
        return (
            "Привет, я игровое поле " f"- {self.side_size}x{self.side_size}!"
            )
