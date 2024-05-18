from sys import maxsize

class GameBoard():
    def __init__(self, reds = {1, 3, 5, 7, 10, 12, 14, 16, 21, 23, 25, 27}, 
                       blues = {50, 52, 54, 56, 61, 63, 65, 67, 70, 72, 74, 76},
                       kingreds = set(), kingblues = set()):
        self.reds = reds
        self.blues = blues
        self.kingreds = kingreds
        self.kingblues = kingblues
    def __eq__(self, board):
        return self.reds == board.reds and self.blues == board.blues and self.kingreds == board.kingreds and self.kingblues == board.kingblues

def heuristic(board):
    if len(board.reds) == 0 and len(board.kingreds) == 0:
        return -maxsize
    if len(board.blues) == 0 and len(board.kingblues) == 0:
        return maxsize
    score = 3 * (len(board.reds) + 2 * len(board.kingreds) - len(board.blues) - 2 * len(board.kingblues))
    borders = [1, 3, 5, 7, 10, 30, 50, 70, 72, 74, 76, 67, 47, 27]
    for i in borders:
        if i in board.reds or i in board.kingreds:
            score += 1
        elif i in board.blues or i in board.kingblues:
            score -= 1
    for figure in board.reds:
        score += figure // 10
        if figure - 9 in board.reds and figure - 11 in board.reds:
            score += 2
    for figure in board.blues:
        score -= (80 - figure) // 10
        if figure + 9 in board.blues and figure + 11 in board.blues:
            score -= 2
    return score