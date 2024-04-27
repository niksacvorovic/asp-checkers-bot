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

def captureplays(board, field, add = []):
    plays = {}
    if ((field - 11) in board.reds or (field - 11) in board.kingreds) and is_empty(field - 22, board) and field % 10 > 1 and field // 10 > 1:
        plays[field - 22] = [field - 11] + add
        plays.update(captureplays(board, field - 22, plays[field - 22]))
    if ((field - 9) in board.reds or (field - 9) in board.kingreds) and is_empty(field - 18, board) and field % 10 < 6 and field // 10 > 1:
        plays[field - 18] = [field - 9] + add
        plays.update(captureplays(board, field - 18, plays[field - 18]))
    if field in board.kingblues:
        if ((field + 11) in board.reds or (field + 11) in board.kingreds) and is_empty(field + 22, board) and field % 10 < 6 and field // 10 < 6:
            plays[field + 22] = [field + 11] + add
            plays.update(captureplays(board, field + 22, plays[field + 22]))
        if ((field + 9) in board.reds or (field + 9) in board.kingreds) and is_empty(field + 18, board) and field % 10 > 1 and field // 10 < 6:
            plays[field + 18] = [field + 9] + add
            plays.update(captureplays(board, field + 18, plays[field + 18]))
    return plays
    
def play(board):
    while True:
        while True:
            tile = str(input("Unesite polje na kojem je žeton koji biste pomerili: "))
            if not(len(tile) == 2 and tile[0].upper() in ["A", "B", "C", "D", "E", "F", "G", "H"] and tile[1] in ["1", "2", "3", "4", "5", "6", "7", "8"]):
                print("Uneli ste neispravno polje")
                continue
            field = convert(tile)
            if field not in board.blues and field not in board.kingblues:
                print("Na datom polju se ne nalazi Vaš žeton")
                continue
            else:
                break
        regplays = regularplays(board, field)
        captplays = captureplays(board, field)
        if regplays == [] and captplays == {}:
            print("Dati žeton se ne može pomeriti")
            continue
        print("Dostupni potezi: ", end = "")
        for p in regplays:
            print(convertback(p), end = " ")
        for p in captplays:
            print(convertback(p), end = " ")
        print()
        while True:
            next = str(input("Unesite polje na koje biste pomerili žeton: "))
            newfield = convert(next)
            if newfield in regplays or newfield in captplays:
                if field in board.blues:
                    board.blues.pop(field)
                    if newfield // 10 == 0:
                        board.kingblues[newfield] = (newfield // 10, newfield % 10)
                    else:
                        board.blues[newfield] = (newfield // 10, newfield % 10)
                elif field in board.kingblues:
                    board.kingblues.pop(field)
                    board.kingblues[newfield] = (newfield // 10, newfield % 10)
                if newfield in captplays:
                    for enemy in captplays[newfield]:
                        if enemy in board.reds:
                            board.reds.pop(enemy)
                        else:
                            board.kingreds.pop(enemy)
                break
            else:
                print("Ne možete odigrati taj potez")
        break