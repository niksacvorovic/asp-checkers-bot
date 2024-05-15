from classes import *
from regplays import *
from captplays import *
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

def minimax(node):
    for child in node.children:
        child.alpha = node.alpha
        child.beta = node.beta
        minimax(child)
    if node.children == []:
        return None
    noderef = None
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
    #if node.level % 2 == 1:
    #    for child in node.children:
    #        if child.value < node.alpha:
    #            node.children.remove(child)
    #        else:
    #            node.alpha = child.value
    #            noderef = child
    #    node.value = node.alpha
    #else:
    #    for child in node.children:
    #        if child.value > node.beta:
    #            node.children.remove(child)
    #        else:
    #            node.beta = child.value
    #            noderef = child
    #    node.value = node.beta
    noderef.mark = True

def botplay(tree):
    minimax(tree.root)
    for child in tree.root.children:
        if child.mark:
            return child.board