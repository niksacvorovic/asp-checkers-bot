from os import system
from mechanisms import printboard, play
from gameboard import GameBoard
from bot import *
from time import time

def main():
    system('cls')
    print("Dobrodošli u igru Dame!")
    print("Odaberite Vaš režim igre")
    print("1. Bez obaveznog preskakanja")
    print("2. Obavezno preskakanje")
    while True:
        args = input("Odaberite režim: ")
        if args in ["1", "2"]:
            break
        else:
            print("Odabrali ste nepostojeću opciju. Pokušajte opet.")
    table = generate_transposition_table()
    cache = {}
    system('cls')
    print("Igra može da počne!")
    board = GameBoard()
    board.hash = hashboard(board, table)
    printboard(board)
    while True:
        play(board, args)
        board.hash = hashboard(board, table)
        cache[board.hash] = board
        system('cls')
        print("Vaš potez: ")
        printboard(board)
        if len(board.reds) == 0 and len(board.kingreds) == 0:
            print("Pobedili ste računar! Čestitamo")
            break
        print("Čeka se protivnički potez...")
        start = time()
        depth = 0
        if args == "1":
            while time() - start < 1:
                depth += 1
                newboard = minimax_alphabeta(board, depth, True, -maxsize, maxsize, table, cache)
                #newboard = minimax(board, depth, True, table, cache)
                if newboard[0] == maxsize:
                    break
                print(time() - start)
        if args == "2":
            while time() - start < 1:
                depth += 1
                newboard = minimax_alphabeta(board, depth, True, -maxsize, maxsize, table, cache)
                #newboard = minimax_aggro(board, depth, True, table, cache)
                print(time() - start)
        board = newboard[1]
        if type(board) == type(None):
            print("Računar ne može odigrati nijedan potez. Pobedili ste računar (nekako)")
            break
        #system('cls')
        print("Protivnički potez:")
        printboard(board)
        if len(board.blues) == 0 and len(board.kingblues) == 0:
            print("Izgubili ste od računara!")
            break

if __name__ == "__main__":
    main()