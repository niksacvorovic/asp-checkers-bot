from classes import *
from mechanisms import is_empty
from copy import deepcopy

def generateregplays(board):
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

def generatecaptplays(board):
    plays = []
    for field in board.reds:
        if (field + 11) in board.blues and is_empty(field + 22, board) and field % 10 < 6 and field // 10 < 6:
            newfield = field + 22
            capture = field + 11
            newreds = deepcopy(board.reds)
            newblues = deepcopy(board.blues)
            newreds.pop(field)
            newblues.pop(capture)
            if newfield < 70:
                newreds[newfield] = (newfield // 10, newfield % 10)
                newboard = GameBoard(newreds, newblues, board.kingreds, board.kingblues)
                plays.append(newboard)
            else:
                newkingreds = deepcopy(board.kingreds)
                newkingreds[newfield] = (newfield // 10, newfield % 10)
                newboard = GameBoard(newreds, newblues, newkingreds, board.kingblues)
                plays.append(newboard)
            plays += generatecaptplays(newboard)
        elif (field + 11) in board.kingblues and is_empty(field + 22, board) and field % 10 < 6 and field // 10 < 6:
            newfield = field + 22
            capture = field + 11
            newreds = deepcopy(board.reds)
            newkingblues = deepcopy(board.kingblues)
            newreds.pop(field)
            newkingblues.pop(capture)
            if newfield < 70:
                newreds[newfield] = (newfield // 10, newfield % 10)
                newboard = GameBoard(newreds, board.blues, board.kingreds, newkingblues)
                plays.append(newboard)
            else:
                newkingreds = deepcopy(board.kingreds)
                newkingreds[newfield] = (newfield // 10, newfield % 10)
                newboard = GameBoard(newreds, board.blues, newkingreds, newkingblues)
                plays.append(newboard)
            plays += generatecaptplays(newboard)
        if (field + 9) in board.blues and is_empty(field + 18, board) and field % 10 > 1 and field // 10 < 6:
            newfield = field + 18
            capture = field + 9
            newreds = deepcopy(board.reds)
            newblues = deepcopy(board.blues)
            newreds.pop(field)
            newblues.pop(capture)
            if newfield < 70:
                newreds[newfield] = (newfield // 10, newfield % 10)
                newboard = GameBoard(newreds, newblues, board.kingreds, board.kingblues)
                plays.append(newboard)
            else:
                newkingreds = deepcopy(board.kingreds)
                newkingreds[newfield] = (newfield // 10, newfield % 10)
                newboard = GameBoard(newreds, newblues, newkingreds, board.kingblues)
                plays.append(newboard)
            plays += generatecaptplays(newboard)
        elif (field + 9) in board.kingblues and is_empty(field + 18, board) and field % 10 > 1 and field // 10 < 6:
            newfield = field + 18
            capture = field + 9
            newreds = deepcopy(board.reds)
            newkingblues = deepcopy(board.kingblues)
            newreds.pop(field)
            newkingblues.pop(capture)
            if newfield < 70:
                newreds[newfield] = (newfield // 10, newfield % 10)
                newboard = GameBoard(newreds, board.blues, board.kingreds, newkingblues)
                plays.append(newboard)
            else:
                newkingreds = deepcopy(board.kingreds)
                newkingreds[newfield] = (newfield // 10, newfield % 10)
                newboard = GameBoard(newreds, board.blues, newkingreds, newkingblues)
                plays.append(newboard)
            plays += generatecaptplays(newboard)
    for field in board.kingreds:
        if (field + 11) in board.blues and is_empty(field + 22, board) and field % 10 < 6 and field // 10 < 6:
            newfield = field + 22
            capture = field + 11
            newkingreds = deepcopy(board.kingreds)
            newblues = deepcopy(board.blues)
            newkingreds.pop(field)
            newblues.pop(capture)
            newkingreds[newfield] = (newfield // 10, newfield % 10)
            newboard = GameBoard(board.reds, newblues, newkingreds, board.kingblues)
            plays.append(newboard)
            plays += generatecaptplays(newboard)
        elif (field + 11) in board.kingblues and is_empty(field + 22, board) and field % 10 < 6 and field // 10 < 6:
            newfield = field + 22
            capture = field + 11
            newkingreds = deepcopy(board.kingreds)
            newkingblues = deepcopy(board.kingblues)
            newkingreds.pop(field)
            newkingblues.pop(capture)
            newkingreds[newfield] = (newfield // 10, newfield % 10)
            newboard = GameBoard(board.reds, board.blues, newkingreds, newkingblues)
            plays.append(newboard)
            plays += generatecaptplays(newboard)
        if (field + 9) in board.blues and is_empty(field + 18, board) and field % 10 > 1 and field // 10 < 6:
            newfield = field + 18
            capture = field + 9
            newkingreds = deepcopy(board.kingreds)
            newblues = deepcopy(board.blues)
            newkingreds.pop(field)
            newblues.pop(capture)
            newkingreds[newfield] = (newfield // 10, newfield % 10)
            newboard = GameBoard(board.reds, newblues, newkingreds, board.kingblues)
            plays.append(newboard)
            plays += generatecaptplays(newboard)
        elif (field + 9) in board.kingblues and is_empty(field + 18, board) and field % 10 > 1 and field // 10 < 6:
            newfield = field + 18
            capture = field + 9
            newkingreds = deepcopy(board.kingreds)
            newkingblues = deepcopy(board.kingblues)
            newkingreds.pop(field)
            newkingblues.pop(capture)
            newkingreds[newfield] = (newfield // 10, newfield % 10)
            newboard = GameBoard(board.reds, board.blues, newkingreds, newkingblues)
            plays.append(newboard)
            plays += generatecaptplays(newboard)
        if (field - 11) in board.blues and is_empty(field - 22, board) and field % 10 > 1 and field // 10 > 1:
            newfield = field - 22
            capture = field - 11
            newkingreds = deepcopy(board.kingreds)
            newblues = deepcopy(board.blues)
            newkingreds.pop(field)
            newblues.pop(capture)
            newkingreds[newfield] = (newfield // 10, newfield % 10)
            newboard = GameBoard(board.reds, newblues, newkingreds, board.kingblues)
            plays.append(newboard)
            plays += generatecaptplays(newboard)
        elif (field - 11) in board.kingblues and is_empty(field - 22, board) and field % 10 > 1 and field // 10 > 1:
            newfield = field - 22
            capture = field - 11
            newkingreds = deepcopy(board.kingreds)
            newkingblues = deepcopy(board.kingblues)
            newkingreds.pop(field)
            newkingblues.pop(capture)
            newkingreds[newfield] = (newfield // 10, newfield % 10)
            newboard = GameBoard(board.reds, board.blues, newkingreds, newkingblues)
            plays.append(newboard)
            plays += generatecaptplays(newboard)
        if (field - 9) in board.blues and is_empty(field - 18, board) and field % 10 < 6 and field // 10 > 1:
            newfield = field - 18
            capture = field - 9
            newkingreds = deepcopy(board.kingreds)
            newblues = deepcopy(board.blues)
            newkingreds.pop(field)
            newblues.pop(capture)
            newkingreds[newfield] = (newfield // 10, newfield % 10)
            newboard = GameBoard(board.reds, newblues, newkingreds, board.kingblues)
            plays.append(newboard)
            plays += generatecaptplays(newboard)
        elif (field - 9) in board.kingblues and is_empty(field - 18, board) and field % 10 < 6 and field // 10 > 1:
            newfield = field - 18
            capture = field - 9
            newkingreds = deepcopy(board.kingreds)
            newkingblues = deepcopy(board.kingblues)
            newkingreds.pop(field)
            newkingblues.pop(capture)
            newkingreds[newfield] = (newfield // 10, newfield % 10)
            newboard = GameBoard(board.reds, board.blues, newkingreds, newkingblues)
            plays.append(newboard)
            plays += generatecaptplays(newboard)
    return plays