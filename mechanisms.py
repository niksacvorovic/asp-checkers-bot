def printboard(board):
    print("  A B C D E F G H")
    for i in range(8):
        print(8-i, end="")
        for j in range(8):
            if 10*i+j in board.reds:
                print("🔴", end = "")
            elif 10*i+j in board.kingreds:
                print("❤️", end = "")
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

def play(board):
    while True:
        while True:
            tile = str(input("Unesite polje na kojem je žeton koji biste pomerili: "))
            if not(len(tile) == 2 and tile[0].upper() in ["A", "B", "C", "D", "E", "F", "G", "H"] and tile[1] in ["1", "2", "3", "4", "5", "6", "7", "8"]):
                print("Uneli ste neispravno polje")
                continue
            pos = convert(tile)
            if pos not in board.blues and pos not in board.kingblues:
                print("Na datom polju se ne nalazi Vaš žeton")
                continue
            else:
                break
        break
