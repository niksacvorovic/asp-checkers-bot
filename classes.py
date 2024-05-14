from sys import maxsize

class GameBoard():
    def __init__(self, reds = {1:(0, 1), 3:(0, 3), 5:(0, 5), 7:(0, 7),
                               10:(1, 0), 12:(1, 2), 14:(1, 4), 16:(1, 6), 
                               21:(2, 1), 23:(2, 3), 25:(2, 5), 27:(2, 7)}, 
                       blues = {50:(5, 0), 52:(5, 2), 54:(5, 4), 56:(5, 6),
                                61:(6, 1), 63:(6, 3), 65:(6, 5), 67:(6, 7),
                                70:(7, 0), 72:(7, 2), 74:(7, 4), 76:(7, 6)},
                       kingreds = {}, kingblues = {}):
        self.reds = reds
        self.blues = blues
        self.kingreds = kingreds
        self.kingblues = kingblues
    def __eq__(self, board):
        return self.reds == board.reds and self.blues == board.blues and self.kingreds == board.kingreds and self.kingblues == board.kingblues

class GameTreeNode():
    def __init__(self, board, level):
        self.board = board
        self.value = self.heuristic()
        self.parent = None
        self.level = level
        self.mark = False
        self.alpha = -maxsize
        self.beta = maxsize
        self.children = []
    def heuristic(self):
        if len(self.board.reds) == 0 and len(self.board.kingreds) == 0:
            return -maxsize
        if len(self.board.blues) == 0 and len(self.board.kingblues) == 0:
            return maxsize
        score = 2 * (len(self.board.reds) + 2 * len(self.board.kingreds) - len(self.board.blues) - 2 * len(self.board.kingblues))
        borders = [1, 3, 5, 7, 10, 30, 50, 70, 72, 74, 76, 67, 47, 27]
        for i in borders:
            if i in self.board.reds or i in self.board.kingreds:
                score += 1
            elif i in self.board.blues or i in self.board.kingblues:
                score -= 1
        return score

class GameTree():
    def __init__(self, root):
        self.root = root
    def append(self, node, newnode):
        node.children.append(newnode)
        newnode.parent = node