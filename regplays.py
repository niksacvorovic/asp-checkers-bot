from classes import *
from mechanisms import is_empty
from copy import deepcopy

def generateregplays_red(board):
    plays = []
    for field in board.reds:
        if is_empty(field + 9, board) and field % 10 != 0 and field // 10 != 7:
            newfield = field + 9
            newreds = deepcopy(board.reds)
            newreds.pop(field)
            if newfield < 70:
                newreds[newfield] = (newfield // 10, newfield % 10)
                plays.append(GameBoard(newreds, board.blues, board.kingreds, board.kingblues))
            else:
                newkingreds = deepcopy(board.kingreds)
                newkingreds[newfield] = (newfield // 10, newfield % 10)
                plays.append(GameBoard(newreds, board.blues, newkingreds, board.kingblues))
        if is_empty(field + 11, board) and field % 10 != 7 and field // 10 != 7:
            newfield = field + 11
            newreds = deepcopy(board.reds)
            newreds.pop(field)
            if newfield < 70:
                newreds[newfield] = (newfield // 10, newfield % 10)
                plays.append(GameBoard(newreds, board.blues, board.kingreds, board.kingblues))
            else:
                newkingreds = deepcopy(board.kingreds)
                newkingreds[newfield] = (newfield // 10, newfield % 10)
                plays.append(GameBoard(newreds, board.blues, newkingreds, board.kingblues))
    for field in board.kingreds:
        if is_empty(field + 9, board) and field % 10 != 0 and field // 10 != 7:
            newfield = field + 9
            newkingreds = deepcopy(board.kingreds)
            newkingreds.pop(field)
            newkingreds[newfield] = (newfield // 10, newfield % 10)
            plays.append(GameBoard(board.reds, board.blues, newkingreds, board.kingblues))
        if is_empty(field + 11, board) and field % 10 != 7 and field // 10 != 7:
            newfield = field + 11
            newkingreds = deepcopy(board.kingreds)
            newkingreds.pop(field)
            newkingreds[newfield] = (newfield // 10, newfield % 10)
            plays.append(GameBoard(board.reds, board.blues, newkingreds, board.kingblues))
        if is_empty(field - 11, board) and field % 10 != 0 and field // 10 != 0:
            newfield = field - 11
            newkingreds = deepcopy(board.kingreds)
            newkingreds.pop(field)
            newkingreds[newfield] = (newfield // 10, newfield % 10)
            plays.append(GameBoard(board.reds, board.blues, newkingreds, board.kingblues))
        if is_empty(field - 9, board) and field % 10 != 7 and field // 10 != 0:
            newfield = field - 9
            newkingreds = deepcopy(board.kingreds)
            newkingreds.pop(field)
            newkingreds[newfield] = (newfield // 10, newfield % 10)
            plays.append(GameBoard(board.reds, board.blues, newkingreds, board.kingblues))
    return plays

def generateregplays_blue(board):
    plays = []
    for field in board.blues:
        if is_empty(field - 9, board) and field % 10 != 7 and field // 10 != 0:
            newfield = field - 9
            newblues = deepcopy(board.blues)
            newblues.pop(field)
            if newfield > 9:
                newblues[newfield] = (newfield // 10, newfield % 10)
                plays.append(GameBoard(board.reds, newblues, board.kingreds, board.kingblues))
            else:
                newkingblues = deepcopy(board.kingblues)
                newkingblues[newfield] = (newfield // 10, newfield % 10)
                plays.append(GameBoard(board.reds, newblues, board.kingreds, newkingblues))
        if is_empty(field - 11, board) and field % 10 != 0 and field // 10 != 0:
            newfield = field - 11
            newblues = deepcopy(board.blues)
            newblues.pop(field)
            if newfield > 9:
                newblues[newfield] = (newfield // 10, newfield % 10)
                plays.append(GameBoard(board.reds, newblues, board.kingreds, board.kingblues))
            else:
                newkingblues = deepcopy(board.kingblues)
                newkingblues[newfield] = (newfield // 10, newfield % 10)
                plays.append(GameBoard(board.reds, newblues, board.kingreds, newkingblues))
    for field in board.kingblues:
        if is_empty(field + 9, board) and field % 10 != 0 and field // 10 != 7:
            newfield = field + 9
            newkingblues = deepcopy(board.kingblues)
            newkingblues.pop(field)
            newkingblues[newfield] = (newfield // 10, newfield % 10)
            plays.append(GameBoard(board.reds, board.blues, board.kingreds, newkingblues))
        if is_empty(field + 11, board) and field % 10 != 7 and field // 10 != 7:
            newfield = field + 11
            newkingblues = deepcopy(board.kingblues)
            newkingblues.pop(field)
            newkingblues[newfield] = (newfield // 10, newfield % 10)
            plays.append(GameBoard(board.reds, board.blues, board.kingreds, newkingblues))
        if is_empty(field - 11, board) and field % 10 != 0 and field // 10 != 0:
            newfield = field - 11
            newkingblues = deepcopy(board.kingblues)
            newkingblues.pop(field)
            newkingblues[newfield] = (newfield // 10, newfield % 10)
            plays.append(GameBoard(board.reds, board.blues, board.kingreds, newkingblues))
        if is_empty(field - 9, board) and field % 10 != 7 and field // 10 != 0:
            newfield = field - 9
            newkingblues = deepcopy(board.kingblues)
            newkingblues.pop(field)
            newkingblues[newfield] = (newfield // 10, newfield % 10)
            plays.append(GameBoard(board.reds, board.blues, board.kingreds, newkingblues))
    return plays