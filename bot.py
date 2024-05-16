from classes import *
from regplays import *
from captplays import *
from mechanisms import printboard
from collections import deque
from sys import maxsize

def generatechildren(node, gametree):
    if node.level % 2 == 0:
        plays = generateregplays_blue(node.board) + generatecaptplays_blue(node.board)
    elif node.level % 2 == 1:
        plays = generateregplays_red(node.board) + generatecaptplays_red(node.board)
    nextlevel = node.level + 1
    for board in plays:
        newnode = GameTreeNode(board, nextlevel)
        gametree.append(node, newnode)

def generateinitialtree():
    rootnode = GameTreeNode(GameBoard(), 0)
    gametree = GameTree(rootnode)
    q = deque()
    q.append(rootnode)
    current = rootnode
    while current.level != 4:
        current = q.popleft()
        generatechildren(current, gametree)
        for node in current.children:
            q.append(node)
    return gametree

def findcurrentmove(board, tree):
    for child in tree.root.children:
        if child.board == board:
            newtree = GameTree(child)
            generatenextlevel(newtree.root, newtree)
    return newtree

def generatenextlevel(node, gametree):
    if node.children == []:
        generatechildren(node, gametree)
    else:
        for child in node.children:
            generatenextlevel(child, gametree)

def minimax_old(node):
    noderef = None
    for child in node.children:
        noderef = minimax_old(child)
    if node.children == []:
        return None
    if node.level % 2 == 1:
        newvalue = -maxsize
        for child in node.children:
            if child.value > newvalue:
                newvalue = child.value
                noderef = child
    else:
        newvalue = maxsize
        for child in node.children:
            if child.value < newvalue:
                newvalue = child.value
                noderef = child
    return noderef

def minimax(node):
    noderef = None
    for child in node.children:
        child.alpha = node.alpha
        child.beta = node.beta
        noderef = minimax(child)
    if node.children == []:
        return None
    if node.level % 2 == 1:
        for child in node.children:
            if child.value > node.alpha:
                node.alpha = child.value
                noderef = child
            if node.beta <= node.alpha:
                noderef = child.parent
                break
    else:
        for child in node.children:
            if child.value < node.beta:
                node.beta = child.value
                noderef = child
            if node.beta <= node.alpha:
                noderef = child.parent
                break
    return noderef

def botplay(tree):
    minimax(tree.root)
    for child in tree.root.children:
        if tree.root.value == child.value:
            board = child.board
            printboard(child.board)
    return board