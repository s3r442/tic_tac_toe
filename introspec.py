from inspect import getsource
from gameparts import PlayGround
import gameparts

game = PlayGround()

print(type(game))

print(isinstance(game, PlayGround))
print(isinstance(game, int))

print(game.__class__)

print(dir(game))

print(game)

print(getsource(game.__class__))

print(gameparts.__all__)
print(gameparts.__doc__)
print(print.__doc__)
