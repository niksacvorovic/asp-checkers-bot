from os import system
from classes import GameBoard
from mechanisms import printboard, play

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
    while True:
        printboard(board)
        play(board)
        #printboard(board)
        #botmove()

if __name__ == "__main__":
    main()