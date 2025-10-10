from gameparts.parts import PlayGround
from gameparts.my_errors import CellOccupedError, FieldIndexError


def save_result(result):
    file = open("game_result.txt", "a", encoding="utf-8")
    file.write(result + "\n")
    file.close()


def your_turn():
    game = PlayGround()
    game.display()
    first_player = "X"
    running = True
    while running:
        print(f"Ход делают {first_player}")
        while True:
            try:
                row = int(input("Введите номер строки: "))
                if row < 0 or row >= game.side_size:
                    raise FieldIndexError
                if isinstance(row, str):
                    raise ValueError
                column = int(input("Введите номер столбца: "))
                if column < 0 or column >= game.side_size:
                    raise FieldIndexError
                if isinstance(column, str):
                    raise ValueError
                if game.board[row][column] != " ":
                    raise CellOccupedError
            except CellOccupedError:
                print("Ячейка занята")
                print("Введите другие координаты.")
                continue
            except FieldIndexError:
                print(
                    "Значение должно быть неотрицательным и меньше "
                    f"{game.side_size}."
                )
                print("Пожалуйста, введите значения для строки и столбца заново.")
                continue
            except ValueError:
                print("Буквы вводить нельзя. Только числа.")
                print("Пожалуйста, введите значения для строки и столбца заново.")
                continue
            except Exception as e:
                print(f"Возникла ошибка: {e}")
                continue
            else:
                break
        game.make_move(row, column, first_player)
        print("Ваш ход выполнен!")
        game.display()
        if game.check_winner(first_player):
            result = f"Победил {first_player}."
            print(result)
            save_result(result)
            running = False
        elif game.is_board_full():
            print("Ничья!")
            running = False
            result = "Ничья"
            print(result)
            save_result(result)
        first_player = "O" if first_player == "X" else "X"


if __name__ == "__main__":
    your_turn()
