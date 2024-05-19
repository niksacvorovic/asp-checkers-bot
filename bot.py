from classes import *
from regplays import *
from captplays import *
from random import getrandbits
from sys import maxsize

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
        elif i in board.blues:
            hash ^= table[i][2]
        elif i in board.blues:
            hash ^= table[i][3]
        else:
            pass
    return hash

def minimax(board, depth, ismax):
    if depth == 0:
        return [heuristic(board)]
    if ismax:
        plays = generateregplays_red(board) + generatecaptplays_red(board)
        if plays == []:
            return [maxsize // 2, None]
        max = -maxsize
        for play in plays:
            value = minimax(play, depth - 1, False)[0]
            if (max < value) ^ (value == -maxsize // 2):
                max = value
                move = play
        return [max, move]
    else:
        plays = generateregplays_blue(board) + generatecaptplays_blue(board)
        if plays == []:
            return [-maxsize // 2, None]
        min = maxsize
        for play in plays:
            value = minimax(play, depth - 1, True)[0]
            if (min > value) ^ (value == maxsize // 2):
                min = value
                move = play
        return [min, move]

def minimax_alphabeta(board, depth, ismax, alpha, beta):
    if depth == 0:
        return [heuristic(board), None]
    if ismax:
        plays = generateregplays_red(board) + generatecaptplays_red(board)
        if plays == []:
            return [0, None]
        move = plays[0]
        for play in plays:
            if beta <= alpha:
                return [alpha, move]
            value = minimax_alphabeta(play, depth - 1, False, alpha, beta)[0]
            if alpha < value:
                alpha = value
                move = play
        return [alpha, move]
    else:
        plays = generateregplays_blue(board) + generatecaptplays_blue(board)
        if plays == []:
            return [0, None]
        move = plays[0]
        for play in plays:
            if beta <= alpha:
                return [beta, move]
            value = minimax_alphabeta(play, depth - 1, True, alpha, beta)[0]
            if beta > value:
                beta = value
                move = play
        return [beta, move]