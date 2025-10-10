class PlayGround:
    """Класс, который описывает игровое поле."""

    side_size = 3

    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, char):
        self.board[row][col] = char

    def display(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def __str__(self):
        return "Привет, я игровое поле " f"- {self.side_size}x{self.side_size}!"

    def is_board_full(self):
        for i in range(self.side_size):
            for j in range(self.side_size):
                if self.board[i][j] == " ":
                    return False
        return True
        
    def check_winner(self, player):
        # Проверка по горизонталям и вертикалям
        for i in range(self.side_size):
            if (all([self.board[i][j] == player for j in range(self.side_size)]) or
                    all([self.board[j][i] == player for j in range(self.side_size)])):
                return True
        if (all([self.board[i][i] == player for i in range(self.side_size)]) or
                all([self.board[i][self.side_size - 1 - i] == player for i in range(self.side_size)])):
            return True
        return False
