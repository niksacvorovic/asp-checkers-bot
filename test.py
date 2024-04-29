from regplays import *
from captplays import *
from mechanisms import *
from classes import *
from bot import *

board = GameBoard()
print("generisanje stabla")
plays = generatetree(board)
print("pretraga stabla")
minimax(plays.root)
print("gotovo!")