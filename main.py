from os import system
from classes import GameBoard
from mechanisms import printboard, play
from bot import *
from time import time

def main():
    system('cls')
    print("Dobrodošli u igru Dame!")
    print("Odaberite Vaš režim igre")
    print("1. Obavezno preskakanje")
    print("2. Bez obaveznog preskakanja")
    while True:
        args = input("Odaberite režim: ")
        if args in ["1", "2"]:
            break
        else:
            print("Odabrali ste nepostojeću opciju. Pokušajte opet.")
    table = generate_transposition_table()
    system('cls')
    print("Igra može da počne!")
    board = GameBoard()
    printboard(board)
    while True:
        play(board)
        system('cls')
        print("Vaš potez: ")
        printboard(board)
        if len(board.reds) == 0 and len(board.kingreds) == 0:
            print("Pobedili ste računar! Čestitamo pojeli ste")
            break
        print("Čeka se protivnički potez...")
        start = time()
        depth = 0
        while time() - start < 2:
            depth += 1
            newboard = minimax_alphabeta(board, depth, True, -maxsize, maxsize)[1]
        board = newboard
        if type(board) == type(None):
            print("Računar ne može odigrati nijedan potez. Pobedili ste računar (nekako)")
            break
        system('cls')
        print("Protivnički potez:")
        printboard(board)
        if len(board.blues) == 0 and len(board.kingblues) == 0:
            print("Izgubili ste od računara! Niste pojeli")
            break

if __name__ == "__main__":
    main()