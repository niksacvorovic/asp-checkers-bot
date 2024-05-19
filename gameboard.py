class GameBoard():
    def __init__(self, reds = {1, 3, 5, 7, 10, 12, 14, 16, 21, 23, 25, 27}, 
                       blues = {50, 52, 54, 56, 61, 63, 65, 67, 70, 72, 74, 76},
                       kingreds = set(), kingblues = set(), hash = 0):
        self.reds = reds
        self.blues = blues
        self.kingreds = kingreds
        self.kingblues = kingblues
        self.hash = hash
    def __eq__(self, board):
        return self.reds == board.reds and self.blues == board.blues and self.kingreds == board.kingreds and self.kingblues == board.kingblues