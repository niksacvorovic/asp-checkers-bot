from classes import *
from regplays import *
from captplays import *
from collections import deque
from sys import maxsize

def generatetree(board):
    rootnode = GameTreeNode(board, True)
    gametree = GameTree(rootnode)
    q = deque()
    q.append((rootnode, 0))
    current = (None, 0)
    count = 0
    while current[1] != 6:
        current = q.popleft()
        if current[1] == 5:
            break
        elif current[1] % 2 == 0:
            plays = generateregplays_red(current[0].board) + generatecaptplays_red(current[0].board)
        elif current[1] % 2 == 1:
            plays = generateregplays_blue(current[0].board) + generatecaptplays_blue(current[0].board)
        move = not current[0].move
        for board in plays:
            newnode = GameTreeNode(board, move)
            gametree.append(current[0], newnode)
            q.append((newnode, current[1] + 1))
            count += 1
    return gametree

def minimax(node):
    for child in node.children:
        minimax(child)
    if node.children == []:
        pass
    if node.move:
        newvalue = -maxsize
        for child in node.children:
            if child.value > newvalue:
                newvalue = child.value
        node.value = newvalue
    else:
        newvalue = maxsize
        for child in node.children:
            if child.value < newvalue:
                newvalue = child.value
        node.value = newvalue

def botplay(board):
    tree = generatetree(board)
    minimax(tree.root)
    for child in tree.root.children:
        if child.value == tree.root.value:
            return child.board