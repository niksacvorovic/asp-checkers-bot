from classes import *
from mechanisms import is_empty
from copy import deepcopy

def generatecaptplays_redfield(board, field):
    plays = []
    if (field + 11) in board.blues and is_empty(field + 22, board) and field % 10 < 6 and field // 10 < 6:
        newfield = field + 22
        capture = field + 11
        newreds = deepcopy(board.reds)
        newblues = deepcopy(board.blues)
        newreds.remove(field)
        newblues.remove(capture)
        if newfield < 70:
            newreds.add(newfield)
            newboard = GameBoard(newreds, newblues, board.kingreds, board.kingblues)
            plays.append(newboard)
        else:
            newkingreds = deepcopy(board.kingreds)
            newkingreds.add(newfield)
            newboard = GameBoard(newreds, newblues, newkingreds, board.kingblues)
            plays.append(newboard)
        plays += generatecaptplays_redfield(newboard, newfield)
    elif (field + 11) in board.kingblues and is_empty(field + 22, board) and field % 10 < 6 and field // 10 < 6:
        newfield = field + 22
        capture = field + 11
        newreds = deepcopy(board.reds)
        newkingblues = deepcopy(board.kingblues)
        newreds.remove(field)
        newkingblues.remove(capture)
        if newfield < 70:
            newreds.add(newfield)
            newboard = GameBoard(newreds, board.blues, board.kingreds, newkingblues)
            plays.append(newboard)
        else:
            newkingreds = deepcopy(board.kingreds)
            newkingreds.add(newfield)
            newboard = GameBoard(newreds, board.blues, newkingreds, newkingblues)
            plays.append(newboard)
        plays += generatecaptplays_redfield(newboard, newfield)
    if (field + 9) in board.blues and is_empty(field + 18, board) and field % 10 > 1 and field // 10 < 6:
        newfield = field + 18
        capture = field + 9
        newreds = deepcopy(board.reds)
        newblues = deepcopy(board.blues)
        newreds.remove(field)
        newblues.remove(capture)
        if newfield < 70:
            newreds.add(newfield)
            newboard = GameBoard(newreds, newblues, board.kingreds, board.kingblues)
            plays.append(newboard)
        else:
            newkingreds = deepcopy(board.kingreds)
            newkingreds.add(newfield)
            newboard = GameBoard(newreds, newblues, newkingreds, board.kingblues)
            plays.append(newboard)
        plays += generatecaptplays_redfield(newboard, newfield)
    elif (field + 9) in board.kingblues and is_empty(field + 18, board) and field % 10 > 1 and field // 10 < 6:
        newfield = field + 18
        capture = field + 9
        newreds = deepcopy(board.reds)
        newkingblues = deepcopy(board.kingblues)
        newreds.remove(field)
        newkingblues.remove(capture)
        if newfield < 70:
            newreds.add(newfield)
            newboard = GameBoard(newreds, board.blues, board.kingreds, newkingblues)
            plays.append(newboard)
        else:
            newkingreds = deepcopy(board.kingreds)
            newkingreds.add(newfield)
            newboard = GameBoard(newreds, board.blues, newkingreds, newkingblues)
            plays.append(newboard)
        plays += generatecaptplays_redfield(newboard, newfield)
    return plays

def generatecaptplays_kingredfield(board, field):
    plays = []
    if (field + 11) in board.blues and is_empty(field + 22, board) and field % 10 < 6 and field // 10 < 6:
        newfield = field + 22
        capture = field + 11
        newkingreds = deepcopy(board.kingreds)
        newblues = deepcopy(board.blues)
        newkingreds.remove(field)
        newblues.remove(capture)
        newkingreds.add(newfield)
        newboard = GameBoard(board.reds, newblues, newkingreds, board.kingblues)
        plays.append(newboard)
        plays += generatecaptplays_kingredfield(newboard, newfield)
    elif (field + 11) in board.kingblues and is_empty(field + 22, board) and field % 10 < 6 and field // 10 < 6:
        newfield = field + 22
        capture = field + 11
        newkingreds = deepcopy(board.kingreds)
        newkingblues = deepcopy(board.kingblues)
        newkingreds.remove(field)
        newkingblues.remove(capture)
        newkingreds.add(newfield)
        newboard = GameBoard(board.reds, board.blues, newkingreds, newkingblues)
        plays.append(newboard)
        plays += generatecaptplays_kingredfield(newboard, newfield)
    if (field + 9) in board.blues and is_empty(field + 18, board) and field % 10 > 1 and field // 10 < 6:
        newfield = field + 18
        capture = field + 9
        newkingreds = deepcopy(board.kingreds)
        newblues = deepcopy(board.blues)
        newkingreds.remove(field)
        newblues.remove(capture)
        newkingreds.add(newfield)
        newboard = GameBoard(board.reds, newblues, newkingreds, board.kingblues)
        plays.append(newboard)
        plays += generatecaptplays_kingredfield(newboard, newfield)
    elif (field + 9) in board.kingblues and is_empty(field + 18, board) and field % 10 > 1 and field // 10 < 6:
        newfield = field + 18
        capture = field + 9
        newkingreds = deepcopy(board.kingreds)
        newkingblues = deepcopy(board.kingblues)
        newkingreds.remove(field)
        newkingblues.remove(capture)
        newkingreds.add(newfield)
        newboard = GameBoard(board.reds, board.blues, newkingreds, newkingblues)
        plays.append(newboard)
        plays += generatecaptplays_kingredfield(newboard, newfield)
    if (field - 11) in board.blues and is_empty(field - 22, board) and field % 10 > 1 and field // 10 > 1:
        newfield = field - 22
        capture = field - 11
        newkingreds = deepcopy(board.kingreds)
        newblues = deepcopy(board.blues)
        newkingreds.remove(field)
        newblues.remove(capture)
        newkingreds.add(newfield)
        newboard = GameBoard(board.reds, newblues, newkingreds, board.kingblues)
        plays.append(newboard)
        plays += generatecaptplays_kingredfield(newboard, newfield)
    elif (field - 11) in board.kingblues and is_empty(field - 22, board) and field % 10 > 1 and field // 10 > 1:
        newfield = field - 22
        capture = field - 11
        newkingreds = deepcopy(board.kingreds)
        newkingblues = deepcopy(board.kingblues)
        newkingreds.remove(field)
        newkingblues.remove(capture)
        newkingreds.add(newfield)
        newboard = GameBoard(board.reds, board.blues, newkingreds, newkingblues)
        plays.append(newboard)
        plays += generatecaptplays_kingredfield(newboard, newfield)
    if (field - 9) in board.blues and is_empty(field - 18, board) and field % 10 < 6 and field // 10 > 1:
        newfield = field - 18
        capture = field - 9
        newkingreds = deepcopy(board.kingreds)
        newblues = deepcopy(board.blues)
        newkingreds.remove(field)
        newblues.remove(capture)
        newkingreds.add(newfield)
        newboard = GameBoard(board.reds, newblues, newkingreds, board.kingblues)
        plays.append(newboard)
        plays += generatecaptplays_kingredfield(newboard, newfield)
    elif (field - 9) in board.kingblues and is_empty(field - 18, board) and field % 10 < 6 and field // 10 > 1:
        newfield = field - 18
        capture = field - 9
        newkingreds = deepcopy(board.kingreds)
        newkingblues = deepcopy(board.kingblues)
        newkingreds.remove(field)
        newkingblues.remove(capture)
        newkingreds.add(newfield)
        newboard = GameBoard(board.reds, board.blues, newkingreds, newkingblues)
        plays.append(newboard)
        plays += generatecaptplays_kingredfield(newboard, newfield)
    return plays

def generatecaptplays_red(board):
    plays = []
    for field in board.reds:
        plays += generatecaptplays_redfield(board, field)
    for field in board.kingreds:
        plays += generatecaptplays_kingredfield(board, field)
    return plays

def generatecaptplays_bluefield(board, field):
    plays = []
    if (field - 11) in board.reds and is_empty(field - 22, board) and field % 10 > 1 and field // 10 > 1:
        newfield = field - 22
        capture = field - 11
        newreds = deepcopy(board.reds)
        newblues = deepcopy(board.blues)
        newreds.remove(capture)
        newblues.remove(field)
        if newfield > 9:
            newblues.add(newfield)
            newboard = GameBoard(newreds, newblues, board.kingreds, board.kingblues)
            plays.append(newboard)
        else:
            newkingblues = deepcopy(board.kingblues)
            newkingblues.add(newfield)
            newboard = GameBoard(newreds, newblues, board.kingreds, newkingblues)
            plays.append(newboard)
        plays += generatecaptplays_bluefield(newboard, newfield)
    elif (field - 11) in board.kingreds and is_empty(field - 22, board) and field % 10 > 1 and field // 10 > 1:
        newfield = field - 22
        capture = field - 11
        newkingreds = deepcopy(board.kingreds)
        newblues = deepcopy(board.blues)
        newkingreds.remove(capture)
        newblues.remove(field)
        if newfield > 9:
            newblues.add(newfield)
            newboard = GameBoard(board.reds, newblues, newkingreds, board.kingblues)
            plays.append(newboard)
        else:
            newkingblues = deepcopy(board.kingblues)
            newkingblues.add(newfield)
            newboard = GameBoard(board.reds, newblues, newkingreds, newkingblues)
            plays.append(newboard)
        plays += generatecaptplays_bluefield(newboard, newfield)
    if (field - 9) in board.reds and is_empty(field - 18, board) and field % 10 < 6 and field // 10 > 1:
        newfield = field - 18
        capture = field - 9
        newreds = deepcopy(board.reds)
        newblues = deepcopy(board.blues)
        newreds.remove(capture)
        newblues.remove(field)
        if newfield > 9:
            newblues.add(newfield)
            newboard = GameBoard(newreds, newblues, board.kingreds, board.kingblues)
            plays.append(newboard)
        else:
            newkingblues = deepcopy(board.kingblues)
            newkingblues.add(newfield)
            newboard = GameBoard(newreds, newblues, board.kingreds, newkingblues)
            plays.append(newboard)
        plays += generatecaptplays_bluefield(newboard, newfield)
    if (field - 9) in board.kingreds and is_empty(field - 18, board) and field % 10 < 6 and field // 10 > 1:
        newfield = field - 18
        capture = field - 9
        newkingreds = deepcopy(board.kingreds)
        newblues = deepcopy(board.blues)
        newkingreds.remove(capture)
        newblues.remove(field)
        if newfield > 9:
            newblues.add(newfield)
            newboard = GameBoard(board.reds, newblues, newkingreds, board.kingblues)
            plays.append(newboard)
        else:
            newkingblues = deepcopy(board.kingblues)
            newkingblues.add(newfield)
            newboard = GameBoard(board.reds, newblues, newkingreds, newkingblues)
            plays.append(newboard)
        plays += generatecaptplays_bluefield(newboard, newfield)
    return plays
    
def generatecaptplays_kingbluefield(board, field):
    plays = []
    if (field + 11) in board.reds and is_empty(field + 22, board) and field % 10 < 6 and field // 10 < 6:
        newfield = field + 22
        capture = field + 11
        newreds = deepcopy(board.reds)
        newkingblues = deepcopy(board.kingblues)
        newreds.remove(capture)
        newkingblues.remove(field)
        newkingblues.add(newfield)
        newboard = GameBoard(newreds, board.blues, board.kingreds, newkingblues)
        plays.append(newboard)
        plays += generatecaptplays_kingbluefield(newboard, newfield)
    elif (field + 11) in board.kingreds and is_empty(field + 22, board) and field % 10 < 6 and field // 10 < 6:
        newfield = field + 22
        capture = field + 11
        newkingreds = deepcopy(board.kingreds)
        newkingblues = deepcopy(board.kingblues)
        newkingreds.remove(capture)
        newkingblues.remove(field)
        newkingblues.add(newfield)
        newboard = GameBoard(board.reds, board.blues, newkingreds, newkingblues)
        plays.append(newboard)
        plays += generatecaptplays_kingbluefield(newboard, newfield)
    if (field + 9) in board.reds and is_empty(field + 18, board) and field % 10 > 1 and field // 10 < 6:
        newfield = field + 18
        capture = field + 9
        newreds = deepcopy(board.reds)
        newkingblues = deepcopy(board.kingblues)
        newreds.remove(capture)
        newkingblues.remove(field)
        newkingblues.add(newfield)
        newboard = GameBoard(newreds, board.blues, board.kingreds, newkingblues)
        plays.append(newboard)
        plays += generatecaptplays_kingbluefield(newboard, newfield)
    elif (field + 9) in board.kingreds and is_empty(field + 18, board) and field % 10 > 1 and field // 10 < 6:
        newfield = field + 18
        capture = field + 9
        newkingreds = deepcopy(board.kingreds)
        newkingblues = deepcopy(board.kingblues)
        newkingreds.remove(capture)
        newkingblues.remove(field)
        newkingblues.add(newfield)
        newboard = GameBoard(board.reds, board.blues, newkingreds, newkingblues)
        plays.append(newboard)
        plays += generatecaptplays_kingbluefield(newboard, newfield)
    if (field - 11) in board.reds and is_empty(field - 22, board) and field % 10 > 1 and field // 10 > 1:
        newfield = field - 22
        capture = field - 11
        newreds = deepcopy(board.reds)
        newkingblues = deepcopy(board.kingblues)
        newreds.remove(capture)
        newkingblues.remove(field)
        newkingblues.add(newfield)
        newboard = GameBoard(newreds, board.blues, board.kingreds, newkingblues)
        plays.append(newboard)
        plays += generatecaptplays_kingbluefield(newboard, newfield)
    elif (field - 11) in board.kingreds and is_empty(field - 22, board) and field % 10 > 1 and field // 10 > 1:
        newfield = field - 22
        capture = field - 11
        newkingreds = deepcopy(board.kingreds)
        newkingblues = deepcopy(board.kingblues)
        newkingreds.remove(capture)
        newkingblues.remove(field)
        newkingblues.add(newfield)
        newboard = GameBoard(board.reds, board.blues, newkingreds, newkingblues)
        plays.append(newboard)
        plays += generatecaptplays_kingbluefield(newboard, newfield)
    if (field - 9) in board.reds and is_empty(field - 18, board) and field % 10 < 6 and field // 10 > 1:
        newfield = field - 18
        capture = field - 9
        newreds = deepcopy(board.reds)
        newkingblues = deepcopy(board.kingblues)
        newreds.remove(capture)
        newkingblues.remove(field)
        newkingblues.add(newfield)
        newboard = GameBoard(newreds, board.blues, board.kingreds, newkingblues)
        plays.append(newboard)
        plays += generatecaptplays_kingbluefield(newboard, newfield)
    elif (field - 9) in board.kingreds and is_empty(field - 18, board) and field % 10 < 6 and field // 10 > 1:
        newfield = field - 18
        capture = field - 9
        newkingreds = deepcopy(board.kingreds)
        newkingblues = deepcopy(board.kingblues)
        newkingreds.remove(capture)
        newkingblues.remove(field)
        newkingblues.add(newfield)
        newboard = GameBoard(board.reds, board.blues, newkingreds, newkingblues)
        plays.append(newboard)
        plays += generatecaptplays_kingbluefield(newboard, newfield)
    return plays

def generatecaptplays_blue(board):
    plays = []
    for field in board.blues:
        plays += generatecaptplays_bluefield(board, field)
    for field in board.kingblues:
        plays += generatecaptplays_kingbluefield(board, field)
    return plays