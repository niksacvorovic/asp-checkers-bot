from classes import *
from mechanisms import is_empty
from copy import deepcopy

def generateregplays_red(board):
    plays = []
    for field in board.reds:
        if is_empty(field + 9, board) and field % 10 != 0 and field // 10 != 7:
            newfield = field + 9
            newreds = deepcopy(board.reds)
            newreds.remove(field)
            if newfield < 70:
                newreds.add(newfield)
                plays.append(GameBoard(newreds, board.blues, board.kingreds, board.kingblues))
            else:
                newkingreds = deepcopy(board.kingreds)
                newkingreds.add(newfield)
                plays.append(GameBoard(newreds, board.blues, newkingreds, board.kingblues))
        if is_empty(field + 11, board) and field % 10 != 7 and field // 10 != 7:
            newfield = field + 11
            newreds = deepcopy(board.reds)
            newreds.remove(field)
            if newfield < 70:
                newreds.add(newfield)
                plays.append(GameBoard(newreds, board.blues, board.kingreds, board.kingblues))
            else:
                newkingreds = deepcopy(board.kingreds)
                newkingreds.add(newfield)
                plays.append(GameBoard(newreds, board.blues, newkingreds, board.kingblues))
    for field in board.kingreds:
        if is_empty(field + 9, board) and field % 10 != 0 and field // 10 != 7:
            newfield = field + 9
            newkingreds = deepcopy(board.kingreds)
            newkingreds.remove(field)
            newkingreds.add(newfield)
            plays.append(GameBoard(board.reds, board.blues, newkingreds, board.kingblues))
        if is_empty(field + 11, board) and field % 10 != 7 and field // 10 != 7:
            newfield = field + 11
            newkingreds = deepcopy(board.kingreds)
            newkingreds.remove(field)
            newkingreds.add(newfield)
            plays.append(GameBoard(board.reds, board.blues, newkingreds, board.kingblues))
        if is_empty(field - 11, board) and field % 10 != 0 and field // 10 != 0:
            newfield = field - 11
            newkingreds = deepcopy(board.kingreds)
            newkingreds.remove(field)
            newkingreds.add(newfield)
            plays.append(GameBoard(board.reds, board.blues, newkingreds, board.kingblues))
        if is_empty(field - 9, board) and field % 10 != 7 and field // 10 != 0:
            newfield = field - 9
            newkingreds = deepcopy(board.kingreds)
            newkingreds.remove(field)
            newkingreds.add(newfield)
            plays.append(GameBoard(board.reds, board.blues, newkingreds, board.kingblues))
    return plays

def generateregplays_blue(board):
    plays = []
    for field in board.blues:
        if is_empty(field - 9, board) and field % 10 != 7 and field // 10 != 0:
            newfield = field - 9
            newblues = deepcopy(board.blues)
            newblues.remove(field)
            if newfield > 9:
                newblues.add(newfield)
                plays.append(GameBoard(board.reds, newblues, board.kingreds, board.kingblues))
            else:
                newkingblues = deepcopy(board.kingblues)
                newkingblues.add(newfield)
                plays.append(GameBoard(board.reds, newblues, board.kingreds, newkingblues))
        if is_empty(field - 11, board) and field % 10 != 0 and field // 10 != 0:
            newfield = field - 11
            newblues = deepcopy(board.blues)
            newblues.remove(field)
            if newfield > 9:
                newblues.add(newfield)
                plays.append(GameBoard(board.reds, newblues, board.kingreds, board.kingblues))
            else:
                newkingblues = deepcopy(board.kingblues)
                newkingblues.add(newfield)
                plays.append(GameBoard(board.reds, newblues, board.kingreds, newkingblues))
    for field in board.kingblues:
        if is_empty(field + 9, board) and field % 10 != 0 and field // 10 != 7:
            newfield = field + 9
            newkingblues = deepcopy(board.kingblues)
            newkingblues.remove(field)
            newkingblues.add(newfield)
            plays.append(GameBoard(board.reds, board.blues, board.kingreds, newkingblues))
        if is_empty(field + 11, board) and field % 10 != 7 and field // 10 != 7:
            newfield = field + 11
            newkingblues = deepcopy(board.kingblues)
            newkingblues.remove(field)
            newkingblues.add(newfield)
            plays.append(GameBoard(board.reds, board.blues, board.kingreds, newkingblues))
        if is_empty(field - 11, board) and field % 10 != 0 and field // 10 != 0:
            newfield = field - 11
            newkingblues = deepcopy(board.kingblues)
            newkingblues.remove(field)
            newkingblues.add(newfield)
            plays.append(GameBoard(board.reds, board.blues, board.kingreds, newkingblues))
        if is_empty(field - 9, board) and field % 10 != 7 and field // 10 != 0:
            newfield = field - 9
            newkingblues = deepcopy(board.kingblues)
            newkingblues.remove(field)
            newkingblues.add(newfield)
            plays.append(GameBoard(board.reds, board.blues, board.kingreds, newkingblues))
    return plays