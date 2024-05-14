from regplays import *
from captplays import *
from mechanisms import *
from classes import *
from bot import *

board = GameBoard()
node = GameTreeNode(board, 0)
tree = GameTree(node)
generatenextlevel(tree.root, tree)
print("gotov nivo 1")
generatenextlevel(tree.root, tree)
print("gotov nivo 2")
generatenextlevel(tree.root, tree)
print("gotov nivo 3")
generatenextlevel(tree.root, tree)
print("gotov nivo 4")
generatenextlevel(tree.root, tree)
print("gotov nivo 5")
newboard = GameBoard({1:(0, 1), 3:(0, 3), 5:(0, 5), 7:(0, 7), 10:(1, 0), 12:(1, 2), 14:(1, 4), 16:(1, 6), 
21:(2, 1), 23:(2, 3), 25:(2, 5), 27:(2, 7)}, {41:(4, 1), 52:(5, 2), 54:(5, 4), 56:(5, 6), 61:(6, 1), 63:(6, 3), 
65:(6, 5), 67:(6, 7), 70:(7, 0), 72:(7, 2), 74:(7, 4), 76:(7, 6)}, {}, {})
tree = findcurrentmove(newboard, tree)
print("nadjeno novo stanje")
generatenextlevel(tree.root, tree)
print("gotov novi 5")