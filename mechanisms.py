def printboard(board):
    print("  A B C D E F G H")
    for i in range(8):
        print(8-i, end="")
        for j in range(8):
            if 10*i+j in board.reds:
                print("🔴", end = "")
            elif 10*i+j in board.kingreds:
                print("❤️", end = " ")
            elif 10*i+j in board.blues:
                print("🔵", end = "")
            elif 10*i+j in board.kingblues:
                print("💙", end = "")
            elif (i+j)%2 == 0:
                print("⬜", end = "")
            else:
                print("⬛", end = "")
        print()

def convert(tile):
    if tile == "x" or tile == "X":
        return -1
    row = 7 - ord(tile[1].upper()) + ord('1')
    col = ord(tile[0].upper()) - ord('A')
    return 10 * row + col

def convertback(field):
    return chr(field % 10 + 65) + chr(7- (field // 10) + 49)

def is_empty(field, board):
    return (field not in board.blues) and (field not in board.kingblues) and (field not in board.reds) and (field not in board.kingreds)

def regularplays(board, field):
    plays = []
    if is_empty(field - 11, board) and field % 10 != 0 and field // 10 != 0:
        plays.append(field - 11)
    if is_empty(field - 9, board) and field % 10 != 7 and field // 10 != 0:
        plays.append(field - 9)
    if field in board.kingblues:
        if is_empty(field + 9, board) and field % 10 != 0 and field // 10 != 7:
            plays.append(field + 9)
        if is_empty(field + 11, board) and field % 10 != 7 and field // 10 != 7:
            plays.append(field + 11)
    return plays

def captureplays(board, field, nextmove, add = []):
    plays = {}
    if ((field - 11) in board.reds or (field - 11) in board.kingreds) and is_empty(field - 22, board) and field % 10 > 1 and field // 10 > 1:
        plays[field - 22] = [field - 11] + add
        plays.update(captureplays(board, field - 22, False, plays[field - 22]))
    if ((field - 9) in board.reds or (field - 9) in board.kingreds) and is_empty(field - 18, board) and field % 10 < 6 and field // 10 > 1:
        plays[field - 18] = [field - 9] + add
        plays.update(captureplays(board, field - 18, False, plays[field - 18]))
    if field in board.kingblues or nextmove:
        if ((field + 11) in board.reds or (field + 11) in board.kingreds) and is_empty(field + 22, board) and field % 10 < 6 and field // 10 < 6:
            plays[field + 22] = [field + 11] + add
            plays.update(captureplays(board, field + 22, True, plays[field + 22]))
        if ((field + 9) in board.reds or (field + 9) in board.kingreds) and is_empty(field + 18, board) and field % 10 > 1 and field // 10 < 6:
            plays[field + 18] = [field + 9] + add
            plays.update(captureplays(board, field + 18, True, plays[field + 18]))
    return plays

def movablefigures(board):
    available = []
    for field in board.blues:
        if is_empty(field - 11, board) and field % 10 != 0 and field // 10 != 0:
            available.append(field)
            continue
        if is_empty(field - 9, board) and field % 10 != 7 and field // 10 != 0:
            available.append(field)
            continue
        if ((field - 11) in board.reds or (field - 11) in board.kingreds) and is_empty(field - 22, board) and field % 10 > 1 and field // 10 > 1:
            available.append(field)
            continue
        if ((field - 9) in board.reds or (field - 9) in board.kingreds) and is_empty(field - 18, board) and field % 10 < 6 and field // 10 > 1:
            available.append(field)
            continue
    for field in board.kingblues:
        if is_empty(field - 11, board) and field % 10 != 0 and field // 10 != 0:
            available.append(field)
            continue
        if is_empty(field - 9, board) and field % 10 != 7 and field // 10 != 0:
            available.append(field)
            continue
        if is_empty(field + 9, board) and field % 10 != 0 and field // 10 != 7:
            available.append(field)
            continue
        if is_empty(field + 11, board) and field % 10 != 7 and field // 10 != 7:
            available.append(field)
            continue
        if ((field - 11) in board.reds or (field - 11) in board.kingreds) and is_empty(field - 22, board) and field % 10 > 1 and field // 10 > 1:
            available.append(field)
            continue
        if ((field - 9) in board.reds or (field - 9) in board.kingreds) and is_empty(field - 18, board) and field % 10 < 6 and field // 10 > 1:
            available.append(field)
            continue
        if ((field + 11) in board.reds or (field + 11) in board.kingreds) and is_empty(field + 22, board) and field % 10 < 6 and field // 10 < 6:
            available.append(field)
            continue
        if ((field + 9) in board.reds or (field + 9) in board.kingreds) and is_empty(field + 18, board) and field % 10 > 1 and field // 10 < 6:
            available.append(field)
            continue
    return available
    
def play(board):
    while True:
        while True:
            available = movablefigures(board)
            if available == []:
                print("Ne možete odigrati nijedan potez. Računar je pobedio (nekako)")
                exit()
            else:
                print("Možete odigrati figurama na sledećim poljima: ", end = "")
                for field in available:
                    print(convertback(field), end = " ")
            tile = str(input("\nUnesite polje na kojem je figura koju biste pomerili: "))
            if not(len(tile) == 2 and tile[0].upper() in ["A", "B", "C", "D", "E", "F", "G", "H"] and tile[1] in ["1", "2", "3", "4", "5", "6", "7", "8"]):
                print("Uneli ste neispravno polje")
                continue
            field = convert(tile)
            if field not in board.blues and field not in board.kingblues:
                print("Na datom polju se ne nalazi Vaša figura")
                continue
            else:
                break
        regplays = regularplays(board, field)
        captplays = captureplays(board, field, False)
        if regplays == [] and captplays == {}:
            print("Data figura se ne može pomeriti")
            continue
        print("Dostupni potezi: ", end = "")
        for p in regplays:
            print(convertback(p), end = " ")
        for p in captplays:
            print(convertback(p), end = " ")
        print()
        while True:
            next = str(input("Unesite polje na koje biste pomerili figuru (ili unesite x da otkažete potez): "))
            try:
                newfield = convert(next)
            except:
                continue
            if newfield in regplays or newfield in captplays or newfield == -1:
                break
            else:
                print("Ne možete odigrati taj potez")
        if newfield == -1:
            continue
        if field in board.blues:
            board.blues.remove(field)
            if newfield // 10 == 0:
                board.kingblues.add(newfield)
            else:
                board.blues.add(newfield)
        elif field in board.kingblues:
            board.kingblues.remove(field)
            board.kingblues.add(newfield)
        if newfield in captplays:
            for enemy in captplays[newfield]:
                if enemy in board.reds:
                    board.reds.remove(enemy)
                else:
                    board.kingreds.remove(enemy)
        break