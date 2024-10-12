# functions
# display
# move
# selected
from Player import Player

class Board:

    def __init__(self):
        self.p1 = Player("white")
        self.p2 = Player("Black")
        pass
    
    def display_players(self):
        self.p1.display()
        self.p2.display()   


    
        