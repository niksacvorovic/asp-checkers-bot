from gameboard import GameBoard
from mechanisms import is_empty
from copy import deepcopy

def generatecaptplays_redfield(board, field, table, cache):
    plays = []
    if (field + 11) in board.blues and is_empty(field + 22, board) and field % 10 < 6 and field // 10 < 6:
        newhash = board.hash
        newfield = field + 22
        capture = field + 11
        newhash ^= table[field][0]
        newhash ^= table[capture][1]
        if newfield < 70:
            newhash ^= table[newfield][0]
        else:
            newhash ^= table[newfield][2]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newreds = deepcopy(board.reds)
            newblues = deepcopy(board.blues)
            newreds.remove(field)
            newblues.remove(capture)
            if newfield < 70:
                newreds.add(newfield)
                newboard = GameBoard(newreds, newblues, board.kingreds, board.kingblues, newhash)
                plays.append(newboard)
            else:
                newkingreds = deepcopy(board.kingreds)
                newkingreds.add(newfield)
                newboard = GameBoard(newreds, newblues, newkingreds, board.kingblues, newhash)
                plays.append(newboard)
        plays += generatecaptplays_redfield(newboard, newfield, table, cache)
    elif (field + 11) in board.kingblues and is_empty(field + 22, board) and field % 10 < 6 and field // 10 < 6:
        newhash = board.hash
        newfield = field + 22
        capture = field + 11
        newhash ^= table[field][0]
        newhash ^= table[capture][3]
        if newfield < 70:
            newhash ^= table[newfield][0]
        else:
            newhash ^= table[newfield][2]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newreds = deepcopy(board.reds)
            newkingblues = deepcopy(board.kingblues)
            newreds.remove(field)
            newkingblues.remove(capture)
            if newfield < 70:
                newreds.add(newfield)
                newboard = GameBoard(newreds, board.blues, board.kingreds, newkingblues, newhash)
                plays.append(newboard)
            else:
                newkingreds = deepcopy(board.kingreds)
                newkingreds.add(newfield)
                newboard = GameBoard(newreds, board.blues, newkingreds, newkingblues, newhash)
                plays.append(newboard)
        plays += generatecaptplays_redfield(newboard, newfield, table, cache)
    if (field + 9) in board.blues and is_empty(field + 18, board) and field % 10 > 1 and field // 10 < 6:
        newhash = board.hash
        newfield = field + 18
        capture = field + 9
        newhash ^= table[field][0]
        newhash ^= table[capture][1]
        if newfield < 70:
            newhash ^= table[newfield][0]
        else:
            newhash ^= table[newfield][2]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newreds = deepcopy(board.reds)
            newblues = deepcopy(board.blues)
            newreds.remove(field)
            newblues.remove(capture)
            if newfield < 70:
                newreds.add(newfield)
                newboard = GameBoard(newreds, newblues, board.kingreds, board.kingblues, newhash)
                plays.append(newboard)
            else:
                newkingreds = deepcopy(board.kingreds)
                newkingreds.add(newfield)
                newboard = GameBoard(newreds, newblues, newkingreds, board.kingblues, newhash)
                plays.append(newboard)
        plays += generatecaptplays_redfield(newboard, newfield, table, cache)
    elif (field + 9) in board.kingblues and is_empty(field + 18, board) and field % 10 > 1 and field // 10 < 6:
        newhash = board.hash
        newfield = field + 18
        capture = field + 9
        newhash ^= table[field][0]
        newhash ^= table[capture][3]
        if newfield < 70:
            newhash ^= table[newfield][0]
        else:
            newhash ^= table[newfield][2]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newreds = deepcopy(board.reds)
            newkingblues = deepcopy(board.kingblues)
            newreds.remove(field)
            newkingblues.remove(capture)
            if newfield < 70:
                newreds.add(newfield)
                newboard = GameBoard(newreds, board.blues, board.kingreds, newkingblues, newhash)
                plays.append(newboard)
            else:
                newkingreds = deepcopy(board.kingreds)
                newkingreds.add(newfield)
                newboard = GameBoard(newreds, board.blues, newkingreds, newkingblues, newhash)
                plays.append(newboard)
        plays += generatecaptplays_redfield(newboard, newfield, table, cache)
    return plays

def generatecaptplays_kingredfield(board, field, table, cache):
    plays = []
    if (field + 11) in board.blues and is_empty(field + 22, board) and field % 10 < 6 and field // 10 < 6:
        newhash = board.hash
        newfield = field + 22
        capture = field + 11
        newhash ^= table[field][2]
        newhash ^= table[capture][1]
        newhash ^= table[newfield][2]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newkingreds = deepcopy(board.kingreds)
            newblues = deepcopy(board.blues)
            newkingreds.remove(field)
            newblues.remove(capture)
            newkingreds.add(newfield)
            newboard = GameBoard(board.reds, newblues, newkingreds, board.kingblues, newhash)
            plays.append(newboard)
        plays += generatecaptplays_kingredfield(newboard, newfield, table, cache)
    elif (field + 11) in board.kingblues and is_empty(field + 22, board) and field % 10 < 6 and field // 10 < 6:
        newhash = board.hash
        newfield = field + 22
        capture = field + 11
        newhash ^= table[field][2]
        newhash ^= table[capture][3]
        newhash ^= table[newfield][2]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newkingreds = deepcopy(board.kingreds)
            newkingblues = deepcopy(board.kingblues)
            newkingreds.remove(field)
            newkingblues.remove(capture)
            newkingreds.add(newfield)
            newboard = GameBoard(board.reds, board.blues, newkingreds, newkingblues, newhash)
            plays.append(newboard)
        plays += generatecaptplays_kingredfield(newboard, newfield, table, cache)
    if (field + 9) in board.blues and is_empty(field + 18, board) and field % 10 > 1 and field // 10 < 6:
        newhash = board.hash
        newfield = field + 18
        capture = field + 9
        newhash ^= table[field][2]
        newhash ^= table[capture][1]
        newhash ^= table[newfield][2]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newkingreds = deepcopy(board.kingreds)
            newblues = deepcopy(board.blues)
            newkingreds.remove(field)
            newblues.remove(capture)
            newkingreds.add(newfield)
            newboard = GameBoard(board.reds, newblues, newkingreds, board.kingblues, newhash)
            plays.append(newboard)
        plays += generatecaptplays_kingredfield(newboard, newfield, table, cache)
    elif (field + 9) in board.kingblues and is_empty(field + 18, board) and field % 10 > 1 and field // 10 < 6:
        newhash = board.hash
        newfield = field + 18
        capture = field + 9
        newhash ^= table[field][2]
        newhash ^= table[capture][3]
        newhash ^= table[newfield][2]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newkingreds = deepcopy(board.kingreds)
            newkingblues = deepcopy(board.kingblues)
            newkingreds.remove(field)
            newkingblues.remove(capture)
            newkingreds.add(newfield)
            newboard = GameBoard(board.reds, board.blues, newkingreds, newkingblues, newhash)
            plays.append(newboard)
        plays += generatecaptplays_kingredfield(newboard, newfield, table, cache)
    if (field - 11) in board.blues and is_empty(field - 22, board) and field % 10 > 1 and field // 10 > 1:
        newhash = board.hash
        newfield = field - 22
        capture = field - 11
        newhash ^= table[field][2]
        newhash ^= table[capture][1]
        newhash ^= table[newfield][2]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newkingreds = deepcopy(board.kingreds)
            newblues = deepcopy(board.blues)
            newkingreds.remove(field)
            newblues.remove(capture)
            newkingreds.add(newfield)
            newboard = GameBoard(board.reds, newblues, newkingreds, board.kingblues, newhash)
            plays.append(newboard)
        plays += generatecaptplays_kingredfield(newboard, newfield, table, cache)
    elif (field - 11) in board.kingblues and is_empty(field - 22, board) and field % 10 > 1 and field // 10 > 1:
        newhash = board.hash
        newfield = field - 22
        capture = field - 11
        newhash ^= table[field][2]
        newhash ^= table[capture][3]
        newhash ^= table[newfield][2]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newkingreds = deepcopy(board.kingreds)
            newkingblues = deepcopy(board.kingblues)
            newkingreds.remove(field)
            newkingblues.remove(capture)
            newkingreds.add(newfield)
            newboard = GameBoard(board.reds, board.blues, newkingreds, newkingblues, newhash)
            plays.append(newboard)
        plays += generatecaptplays_kingredfield(newboard, newfield, table, cache)
    if (field - 9) in board.blues and is_empty(field - 18, board) and field % 10 < 6 and field // 10 > 1:
        newhash = board.hash
        newfield = field - 18
        capture = field - 9
        newhash ^= table[field][2]
        newhash ^= table[capture][1]
        newhash ^= table[newfield][2]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newkingreds = deepcopy(board.kingreds)
            newblues = deepcopy(board.blues)
            newkingreds.remove(field)
            newblues.remove(capture)
            newkingreds.add(newfield)
            newboard = GameBoard(board.reds, newblues, newkingreds, board.kingblues, newhash)
            plays.append(newboard)
        plays += generatecaptplays_kingredfield(newboard, newfield, table, cache)
    elif (field - 9) in board.kingblues and is_empty(field - 18, board) and field % 10 < 6 and field // 10 > 1:
        newhash = board.hash
        newfield = field - 18
        capture = field - 9
        newhash ^= table[field][2]
        newhash ^= table[capture][3]
        newhash ^= table[newfield][2]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newkingreds = deepcopy(board.kingreds)
            newkingblues = deepcopy(board.kingblues)
            newkingreds.remove(field)
            newkingblues.remove(capture)
            newkingreds.add(newfield)
            newboard = GameBoard(board.reds, board.blues, newkingreds, newkingblues, newhash)
            plays.append(newboard)
        plays += generatecaptplays_kingredfield(newboard, newfield, table, cache)
    return plays

def generatecaptplays_red(board, table, cache):
    plays = []
    for field in board.reds:
        plays += generatecaptplays_redfield(board, field, table, cache)
    for field in board.kingreds:
        plays += generatecaptplays_kingredfield(board, field, table, cache)
    return plays

def generatecaptplays_bluefield(board, field, table, cache):
    plays = []
    if (field - 11) in board.reds and is_empty(field - 22, board) and field % 10 > 1 and field // 10 > 1:
        newhash = board.hash
        newfield = field - 22
        capture = field - 11
        newhash ^= table[field][1]
        newhash ^= table[capture][0]
        if newfield > 9:
            newhash ^= table[newfield][1]
        else:
            newhash ^= table[newfield][3]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newreds = deepcopy(board.reds)
            newblues = deepcopy(board.blues)
            newreds.remove(capture)
            newblues.remove(field)
            if newfield > 9:
                newblues.add(newfield)
                newboard = GameBoard(newreds, newblues, board.kingreds, board.kingblues, newhash)
                plays.append(newboard)
            else:
                newkingblues = deepcopy(board.kingblues)
                newkingblues.add(newfield)
                newboard = GameBoard(newreds, newblues, board.kingreds, newkingblues, newhash)
                plays.append(newboard)
        plays += generatecaptplays_bluefield(newboard, newfield, table, cache)
    elif (field - 11) in board.kingreds and is_empty(field - 22, board) and field % 10 > 1 and field // 10 > 1:
        newhash = board.hash
        newfield = field - 22
        capture = field - 11
        newhash ^= table[field][1]
        newhash ^= table[capture][2]
        if newfield > 9:
            newhash ^= table[newfield][1]
        else:
            newhash ^= table[newfield][3]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newkingreds = deepcopy(board.kingreds)
            newblues = deepcopy(board.blues)
            newkingreds.remove(capture)
            newblues.remove(field)
            if newfield > 9:
                newblues.add(newfield)
                newboard = GameBoard(board.reds, newblues, newkingreds, board.kingblues, newhash)
                plays.append(newboard)
            else:
                newkingblues = deepcopy(board.kingblues)
                newkingblues.add(newfield)
                newboard = GameBoard(board.reds, newblues, newkingreds, newkingblues, newhash)
                plays.append(newboard)
        plays += generatecaptplays_bluefield(newboard, newfield, table, cache)
    if (field - 9) in board.reds and is_empty(field - 18, board) and field % 10 < 6 and field // 10 > 1:
        newhash = board.hash
        newfield = field - 18
        capture = field - 9
        newhash ^= table[field][1]
        newhash ^= table[capture][0]
        if newfield > 9:
            newhash ^= table[newfield][1]
        else:
            newhash ^= table[newfield][3]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newreds = deepcopy(board.reds)
            newblues = deepcopy(board.blues)
            newreds.remove(capture)
            newblues.remove(field)
            if newfield > 9:
                newblues.add(newfield)
                newboard = GameBoard(newreds, newblues, board.kingreds, board.kingblues, newhash)
                plays.append(newboard)
            else:
                newkingblues = deepcopy(board.kingblues)
                newkingblues.add(newfield)
                newboard = GameBoard(newreds, newblues, board.kingreds, newkingblues, newhash)
                plays.append(newboard)
        plays += generatecaptplays_bluefield(newboard, newfield, table, cache)
    if (field - 9) in board.kingreds and is_empty(field - 18, board) and field % 10 < 6 and field // 10 > 1:
        newhash = board.hash
        newfield = field - 18
        capture = field - 9
        newhash ^= table[field][1]
        newhash ^= table[capture][2]
        if newfield > 9:
            newhash ^= table[newfield][1]
        else:
            newhash ^= table[newfield][3]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newkingreds = deepcopy(board.kingreds)
            newblues = deepcopy(board.blues)
            newkingreds.remove(capture)
            newblues.remove(field)
            if newfield > 9:
                newblues.add(newfield)
                newboard = GameBoard(board.reds, newblues, newkingreds, board.kingblues, newhash)
                plays.append(newboard)
            else:
                newkingblues = deepcopy(board.kingblues)
                newkingblues.add(newfield)
                newboard = GameBoard(board.reds, newblues, newkingreds, newkingblues, newhash)
                plays.append(newboard)
        plays += generatecaptplays_bluefield(newboard, newfield, table, cache)
    return plays
    
def generatecaptplays_kingbluefield(board, field, table, cache):
    plays = []
    if (field + 11) in board.reds and is_empty(field + 22, board) and field % 10 < 6 and field // 10 < 6:
        newhash = board.hash
        newfield = field + 22
        capture = field + 11
        newhash ^= table[field][3]
        newhash ^= table[capture][0]
        newhash ^= table[newfield][3]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newreds = deepcopy(board.reds)
            newkingblues = deepcopy(board.kingblues)
            newreds.remove(capture)
            newkingblues.remove(field)
            newkingblues.add(newfield)
            newboard = GameBoard(newreds, board.blues, board.kingreds, newkingblues, newhash)
            plays.append(newboard)
        plays += generatecaptplays_kingbluefield(newboard, newfield, table, cache)
    elif (field + 11) in board.kingreds and is_empty(field + 22, board) and field % 10 < 6 and field // 10 < 6:
        newhash = board.hash
        newfield = field + 22
        capture = field + 11
        newhash ^= table[field][3]
        newhash ^= table[capture][2]
        newhash ^= table[newfield][3]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newkingreds = deepcopy(board.kingreds)
            newkingblues = deepcopy(board.kingblues)
            newkingreds.remove(capture)
            newkingblues.remove(field)
            newkingblues.add(newfield)
            newboard = GameBoard(board.reds, board.blues, newkingreds, newkingblues, newhash)
            plays.append(newboard)
        plays += generatecaptplays_kingbluefield(newboard, newfield, table, cache)
    if (field + 9) in board.reds and is_empty(field + 18, board) and field % 10 > 1 and field // 10 < 6:
        newhash = board.hash
        newfield = field + 18
        capture = field + 9
        newhash ^= table[field][3]
        newhash ^= table[capture][0]
        newhash ^= table[newfield][3]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newreds = deepcopy(board.reds)
            newkingblues = deepcopy(board.kingblues)
            newreds.remove(capture)
            newkingblues.remove(field)
            newkingblues.add(newfield)
            newboard = GameBoard(newreds, board.blues, board.kingreds, newkingblues, newhash)
            plays.append(newboard)
        plays += generatecaptplays_kingbluefield(newboard, newfield, table, cache)
    elif (field + 9) in board.kingreds and is_empty(field + 18, board) and field % 10 > 1 and field // 10 < 6:
        newhash = board.hash
        newfield = field + 18
        capture = field + 9
        newhash ^= table[field][3]
        newhash ^= table[capture][2]
        newhash ^= table[newfield][3]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newkingreds = deepcopy(board.kingreds)
            newkingblues = deepcopy(board.kingblues)
            newkingreds.remove(capture)
            newkingblues.remove(field)
            newkingblues.add(newfield)
            newboard = GameBoard(board.reds, board.blues, newkingreds, newkingblues, newhash)
            plays.append(newboard)
        plays += generatecaptplays_kingbluefield(newboard, newfield, table, cache)
    if (field - 11) in board.reds and is_empty(field - 22, board) and field % 10 > 1 and field // 10 > 1:
        newhash = board.hash
        newfield = field - 22
        capture = field - 11
        newhash ^= table[field][3]
        newhash ^= table[capture][0]
        newhash ^= table[newfield][3]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newreds = deepcopy(board.reds)
            newkingblues = deepcopy(board.kingblues)
            newreds.remove(capture)
            newkingblues.remove(field)
            newkingblues.add(newfield)
            newboard = GameBoard(newreds, board.blues, board.kingreds, newkingblues, newhash)
        plays.append(newboard)
        plays += generatecaptplays_kingbluefield(newboard, newfield, table, cache)
    elif (field - 11) in board.kingreds and is_empty(field - 22, board) and field % 10 > 1 and field // 10 > 1:
        newhash = board.hash
        newfield = field - 22
        capture = field - 11
        newhash ^= table[field][3]
        newhash ^= table[capture][2]
        newhash ^= table[newfield][3]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newkingreds = deepcopy(board.kingreds)
            newkingblues = deepcopy(board.kingblues)
            newkingreds.remove(capture)
            newkingblues.remove(field)
            newkingblues.add(newfield)
            newboard = GameBoard(board.reds, board.blues, newkingreds, newkingblues, newhash)
            plays.append(newboard)
        plays += generatecaptplays_kingbluefield(newboard, newfield, table, cache)
    if (field - 9) in board.reds and is_empty(field - 18, board) and field % 10 < 6 and field // 10 > 1:
        newhash = board.hash
        newfield = field - 18
        capture = field - 9
        newhash ^= table[field][3]
        newhash ^= table[capture][0]
        newhash ^= table[newfield][3]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newreds = deepcopy(board.reds)
            newkingblues = deepcopy(board.kingblues)
            newreds.remove(capture)
            newkingblues.remove(field)
            newkingblues.add(newfield)
            newboard = GameBoard(newreds, board.blues, board.kingreds, newkingblues, newhash)
            plays.append(newboard)
        plays += generatecaptplays_kingbluefield(newboard, newfield, table, cache)
    elif (field - 9) in board.kingreds and is_empty(field - 18, board) and field % 10 < 6 and field // 10 > 1:
        newhash = board.hash
        newfield = field - 18
        capture = field - 9
        newhash ^= table[field][3]
        newhash ^= table[capture][2]
        newhash ^= table[newfield][3]
        if newhash in cache:
            newboard = cache[newhash]
            plays.append(newboard)
        else:
            newkingreds = deepcopy(board.kingreds)
            newkingblues = deepcopy(board.kingblues)
            newkingreds.remove(capture)
            newkingblues.remove(field)
            newkingblues.add(newfield)
            newboard = GameBoard(board.reds, board.blues, newkingreds, newkingblues, newhash)
            plays.append(newboard)
        plays += generatecaptplays_kingbluefield(newboard, newfield, table, cache)
    return plays

def generatecaptplays_blue(board, table, cache):
    plays = []
    for field in board.blues:
        plays += generatecaptplays_bluefield(board, field, table, cache)
    for field in board.kingblues:
        plays += generatecaptplays_kingbluefield(board, field, table, cache)
    return plays