from os import system
from classes import GameBoard, GameTree
from mechanisms import printboard, play
from bot import *

def main():
    args = 0
    system('cls')
    print("Dobrodošli u igru Dame!")
    print("Odaberite Vaš režim igre")
    print("1. Obavezno preskakanje")
    print("2. Bez obaveznog preskakanja")
    while True:
        args = int(input("Odaberite režim: "))
        if args in [1, 2]:
            break
        else:
            print("Odabrali ste nepostojeću opciju. Pokušajte opet.")
    system('cls')
    print("Igra može da počne!")
    board = GameBoard()
    tree = generateinitialtree()
    printboard(board)
    while True:
        play(board)
        system('cls')
        printboard(board)
        if len(board.reds) == 0 and len(board.kingreds) == 0:
            print("Pobedili ste računar! Čestitamo pojeli ste")
            break
        print("Čeka se protivnički potez...")
        tree = findcurrentmove(board, tree)
        board = botplay(tree)
        system('cls')
        tree = findcurrentmove(board, tree)
        print("Protivnički potez:")
        printboard(board)
        if len(board.blues) == 0 and len(board.kingblues) == 0:
            print("Izgubili ste od računara! Niste pojeli")
            break

if __name__ == "__main__":
    main()