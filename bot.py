from regplays import *
from captplays import *
from random import getrandbits
from sys import maxsize

def heuristic(board):
    if len(board.reds) == 0 and len(board.kingreds) == 0:
        return -maxsize
    if len(board.blues) == 0 and len(board.kingblues) == 0:
        return maxsize
    score = 4 * (len(board.reds) + 2 * len(board.kingreds) - len(board.blues) - 2 * len(board.kingblues))
    borders = [1, 3, 5, 7, 10, 30, 50, 70, 72, 74, 76, 67, 47, 27]
    for i in borders:
        if i in board.reds or i in board.kingreds:
            score += 1
        elif i in board.blues or i in board.kingblues:
            score -= 1
    for figure in board.reds:
        score += figure // 10
        if figure - 9 in board.reds and figure - 11 in board.reds:
            score += 2
    for figure in board.blues:
        score -= (80 - figure) // 10
        if figure + 9 in board.blues and figure + 11 in board.blues:
            score -= 2
    return score

def generate_transposition_table():
    arr = [1, 3, 5, 7, 10, 12, 14, 16, 21, 23, 25, 27, 30, 32, 34, 36, 
           41, 43, 45, 47, 50, 52, 54, 56, 61, 63, 65, 67, 70, 72, 74, 76]
    table = {}
    for field in arr:
        table[field]= [getrandbits(64), getrandbits(64), getrandbits(64), getrandbits(64)]
    return table

def hashboard(board, table):
    hash = 0
    arr = [1, 3, 5, 7, 10, 12, 14, 16, 21, 23, 25, 27, 30, 32, 34, 36, 
           41, 43, 45, 47, 50, 52, 54, 56, 61, 63, 65, 67, 70, 72, 74, 76]
    for i in arr:
        if i in board.reds:
            hash ^= table[i][0]
        elif i in board.blues:
            hash ^= table[i][1]
        elif i in board.kingreds:
            hash ^= table[i][2]
        elif i in board.kingblues:
            hash ^= table[i][3]
        else:
            pass
    return hash

def minimax(board, depth, ismax, table, cache):
    if depth == 0:
        return [heuristic(board)]
    if ismax:
        plays = generateregplays_red(board, table, cache) + generatecaptplays_red(board, table, cache)
        if plays == []:
            return [0, board]
        max = -maxsize
        for play in plays:
            value = minimax(play, depth - 1, False, table, cache)[0]
            if max < value:
                max = value
                move = play
        return [max, move]
    else:
        plays = generateregplays_blue(board, table, cache) + generatecaptplays_blue(board, table, cache)
        if plays == []:
            return [0, board]
        min = maxsize
        for play in plays:
            value = minimax(play, depth - 1, True, table, cache)[0]
            if min > value:
                min = value
                move = play
        return [min, move]

def minimax_alphabeta(board, depth, ismax, alpha, beta, table, cache):
    if depth == 0:
        return [heuristic(board), None]
    if ismax:
        plays = generateregplays_red(board, table, cache) + generatecaptplays_red(board, table, cache)
        if plays == []:
            return [0, board]
        move = None
        for play in plays:
            if beta <= alpha:
                return [alpha, move]
            value = minimax_alphabeta(board, table, cache, depth - 1, ismax, alpha, beta)[0]
            if alpha < value:
                alpha = value
                move = play
        return [alpha, move]
    else:
        plays = generateregplays_blue(board, table, cache) + generatecaptplays_blue(board, table, cache)
        if plays == []:
            return [0, board]
        move = None
        for play in plays:
            if beta <= alpha:
                return [beta, move]
            value = minimax_alphabeta(board, table, cache, depth, ismax, alpha, beta)[0]
            if beta > value:
                beta = value
                move = play
        return [beta, move]