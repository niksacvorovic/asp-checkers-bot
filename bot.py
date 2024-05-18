from classes import *
from regplays import *
from captplays import *
from sys import maxsize

#def minimax_old(node):
#    noderef = None
#    for child in node.children:
#        noderef = minimax_old(child)
#    if node.children == []:
#        return None
#    if node.level % 2 == 1:
#        newvalue = -maxsize
#        for child in node.children:
#            if child.value > newvalue:
#                newvalue = child.value
#                noderef = child
#    else:
#        newvalue = maxsize
#        for child in node.children:
#            if child.value < newvalue:
#                newvalue = child.value
#                noderef = child
#    return noderef

def generate_transposition_table():
    pass

def minimax(board, depth, ismax):
    if depth == 0:
        return [heuristic(board)]
    if ismax:
        plays = generateregplays_red(board) + generatecaptplays_red(board)
        if plays == []:
            return [maxsize, None]
        max = -maxsize
        for play in plays:
            value = minimax(play, depth - 1, False)[0]
            if (max < value) ^ (value == -maxsize):
                max = value
                move = play
        return [max, move]
    else:
        plays = generateregplays_blue(board) + generatecaptplays_blue(board)
        if plays == []:
            return [-maxsize, None]
        min = maxsize
        for play in plays:
            value = minimax(play, depth - 1, True)[0]
            if (min > value) ^ (value == maxsize):
                min = value
                move = play
        return [min, move]

def minimax_alphabeta(board, depth, ismax, alpha, beta):
    if depth == 0:
        return [heuristic(board), None]
    if ismax:
        plays = generateregplays_red(board) + generatecaptplays_red(board)
        if plays == []:
            return [maxsize, None]
        for play in plays:
            ret = minimax_alphabeta(play, depth - 1, False, alpha, beta)
            value = ret[0]
            if type(ret[1]) == type(None):
                move = ret[1]
            if (alpha < value)  ^ (value == -maxsize):
                alpha = value
                move = play
                if beta <= alpha:
                    return [alpha, move]
        return [alpha, move]
    else:
        plays = generateregplays_blue(board) + generatecaptplays_blue(board)
        if plays == []:
            return [-maxsize, None]
        for play in plays:
            ret = minimax_alphabeta(play, depth - 1, False, alpha, beta)
            value = ret[0]
            if type(ret[1]) == type(None):
                move = ret[1]
            if (beta > value) ^ (value == maxsize):
                beta = value
                move = play
                if beta <= alpha:
                    return [alpha, move]
        return [beta, move]

#def minimax(node):
#    noderef = None
#    for child in node.children:
#        child.alpha = node.alpha
#        child.beta = node.beta
#        noderef = minimax(child)
#    if node.children == []:
#        return None
#    if node.level % 2 == 1:
#        for child in node.children:
#            if child.value > node.alpha:
#                node.alpha = child.value
#                noderef = child
#            if node.beta <= node.alpha:
#                noderef = child.parent
#                break
#    else:
#        for child in node.children:
#            if child.value < node.beta:
#                node.beta = child.value
#                noderef = child
#            if node.beta <= node.alpha:
#                noderef = child.parent
#                break
#    return noderef