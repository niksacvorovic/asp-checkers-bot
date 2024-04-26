class GameBoard():
    def __init__(self, reds = {50:(0, 1), 3:(0, 3), 5:(0, 5), 7:(0, 7),
                               10:(1, 0), 32:(1, 2), 14:(1, 4), 16:(1, 6), 
                               21:(2, 1), 23:(2, 3), 25:(2, 5), 27:(2, 7)}, 
                       blues = {12:(5, 0), 52:(5, 2), 54:(5, 4), 56:(5, 6),
                                61:(6, 1), 63:(6, 3), 65:(6, 5), 67:(6, 7),
                                70:(7, 0), 72:(7, 2), 74:(7, 4), 76:(7, 6)},
                       kingreds = {}, kingblues = {}):
        self.reds = reds
        self.blues = blues
        self.kingreds = kingreds
        self.kingblues = kingblues