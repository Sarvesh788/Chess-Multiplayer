from Knight import Knight
from Bishop import Bishop
from King import King
from Queen import Queen
from Pawn import Pawn
from Rook import Rook


class Player:
    def __init__(self, color):
        if color == "black":
            self.k1 = Knight(1, 7)
            self.k2 = Knight(6, 7)
            self.b1 = Bishop(2, 7)
            self.b2 = Bishop(5, 7)
            self.r1 = Rook(0, 7)
            self.r2 = Rook(7, 7)
            self.k = King(4, 7)
            self.q = Queen(3, 7)
            self.p = [Pawn(i, 6) for i in range(8)]
        else:
            self.k1 = Knight(1, 0)
            self.k2 = Knight(6, 0)
            self.b1 = Bishop(2, 0)
            self.b2 = Bishop(5, 0)
            self.r1 = Rook(0, 0)
            self.r2 = Rook(7, 0)
            self.k = King(4, 0)
            self.q = Queen(3, 0)
            self.p = [Pawn(i, 1) for i in range(8)]
        self.color = color
        
    def display(self):
        print(f"Player color: {self.color}")
        self.k1.display()
        self.k2.display()
        self.b1.display()
        self.b2.display()
        self.r1.display()
        self.r2.display()
        self.k.display()
        self.q.display()
    
    def get_position(self):
        self.position = []
        self.position.append(self.k1.get_position())
        self.position.append(self.k2.get_position())
        self.position.append(self.b1.get_position())
        self.position.append(self.b2.get_position())
        self.position.append(self.r1.get_position())
        self.position.append(self.r2.get_position())
        self.position.append(self.k.get_position())
        self.position.append(self.q.get_position())

    def get_king_pos(self):
        return self.k.get_position()
    
    def get_queen_pos(self):
        return self.q.get_position()
    
    def get_knight_pos(self):
        return [self.k1.get_position(), self.k2.get_position()]
    
    def get_bishop_pos(self):
        return [self.b1.get_position(), self.b2.get_position()]
    
    def get_rook_pos(self):
        return [self.r1.get_position(), self.r2.get_position()]
    
    def get_player_color(self):
        return self.color
    
    def get_pawn_pos(self):
        return [i.get_position() for i in self.p]

    def move(self, board, move):
        board.push(move)
        print(board)





