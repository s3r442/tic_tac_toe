from gameparts import PlayGround

game = PlayGround()
game.display()
game.make_move(1, 1, "X")
print("Ход сделан!")
game.display()
