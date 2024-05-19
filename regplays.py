from gameboard import GameBoard
from mechanisms import is_empty
from copy import deepcopy

def generateregplays_redfield(field, step, board, table, cache):
    newhash = board.hash
    newhash ^= table[field][0]
    newfield = field + step
    if newfield < 70:
        newhash ^= table[newfield][0]
    else:
        newhash ^= table[newfield][2]
    if newhash in cache:
        return cache[newhash]
    else:
        newreds = deepcopy(board.reds)
        newreds.remove(field)
        if newfield < 70:
            newreds.add(newfield)
            newboard = GameBoard(newreds, board.blues, board.kingreds, board.kingblues, newhash)
        else:
            newkingreds = deepcopy(board.kingreds)
            newkingreds.add(newfield)
            newboard = GameBoard(newreds, board.blues, newkingreds, board.kingblues, newhash)
        cache[newhash] = newboard
        return newboard
    
def generateregplays_kingredfield(field, step, board, table, cache):
    newhash = board.hash
    newhash ^= table[field][2]
    newfield = field + step
    newhash ^= table[newfield][2]
    if newhash in cache:
        return cache[newhash]
    else:
        newkingreds = deepcopy(board.kingreds)
        newkingreds.remove(field)
        newkingreds.add(newfield)
        newboard = GameBoard(board.reds, board.blues, newkingreds, board.kingblues, newhash)
        cache[newhash] = newboard
        return newboard
        
def generateregplays_bluefield(field, step, board, table, cache):
    newhash = board.hash
    newhash ^= table[field][1]
    newfield = field + step
    if newfield > 9:
        newhash ^= table[newfield][1]
    else:
        newhash ^= table[newfield][3]
    if newhash in cache:
        return cache[newhash]
    else:
        newblues = deepcopy(board.blues)
        newblues.remove(field)
        if newfield > 9:
            newblues.add(newfield)
            newboard = GameBoard(board.reds, newblues, board.kingreds, board.kingblues, newhash)
        else:
            newkingblues = deepcopy(board.kingblues)
            newkingblues.add(newfield)
            newboard = GameBoard(board.reds, newblues, board.kingreds, newkingblues, newhash)
        cache[newhash] = newboard 
        return newboard
    
def generateregplays_kingbluefield(field, step, board, table, cache):
    newhash = board.hash
    newhash ^= table[field][3]
    newfield = field + step
    newhash ^= table[newfield][3]
    if newhash in cache:
        return cache[newhash]
    else:
        newkingblues = deepcopy(board.kingblues)
        newkingblues.remove(field)
        newkingblues.add(newfield)
        newboard = GameBoard(board.reds, board.blues, board.kingreds, newkingblues, newhash)
        cache[newhash] = newboard
        return newboard

def generateregplays_red(board, table, cache):
    plays = []
    for field in board.reds:
        if is_empty(field + 9, board) and field % 10 != 0 and field // 10 != 7:
            plays.append(generateregplays_redfield(field, 9, board, table, cache))
        if is_empty(field + 11, board) and field % 10 != 7 and field // 10 != 7:
            plays.append(generateregplays_redfield(field, 11, board, table, cache))
    for field in board.kingreds:
        if is_empty(field + 9, board) and field % 10 != 0 and field // 10 != 7:
            plays.append(generateregplays_kingredfield(field, 9, board, table, cache))
        if is_empty(field + 11, board) and field % 10 != 7 and field // 10 != 7:
            plays.append(generateregplays_kingredfield(field, 11, board, table, cache))
        if is_empty(field - 11, board) and field % 10 != 0 and field // 10 != 0:
            plays.append(generateregplays_kingredfield(field, -11, board, table, cache))
        if is_empty(field - 9, board) and field % 10 != 7 and field // 10 != 0:
            plays.append(generateregplays_kingredfield(field, -9, board, table, cache))
    return plays

def generateregplays_blue(board, table, cache):
    plays = []
    for field in board.blues:
        if is_empty(field - 9, board) and field % 10 != 7 and field // 10 != 0:
            plays.append(generateregplays_bluefield(field, -9, board, table, cache))
        if is_empty(field - 11, board) and field % 10 != 0 and field // 10 != 0:
            plays.append(generateregplays_bluefield(field, -11, board, table, cache))    
    for field in board.kingblues:
        if is_empty(field + 9, board) and field % 10 != 0 and field // 10 != 7:
            plays.append(generateregplays_kingbluefield(field, 9, board, table, cache))
        if is_empty(field + 11, board) and field % 10 != 7 and field // 10 != 7:
            plays.append(generateregplays_kingbluefield(field, 11, board, table, cache))
        if is_empty(field - 11, board) and field % 10 != 0 and field // 10 != 0:
            plays.append(generateregplays_kingbluefield(field, -11, board, table, cache))
        if is_empty(field - 9, board) and field % 10 != 7 and field // 10 != 0:
            plays.append(generateregplays_kingbluefield(field, -9, board, table, cache))
    return plays