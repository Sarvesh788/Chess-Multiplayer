# move
# position


class Pawn:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True

    def display(self):
        print(f"The position of Knight is{self.x}, {self.y}")

    def get_position(self):
        return self.x, self.y
    
    def is_alive(self):
        return self.alive
    
    def kill(self):
        self.alive = False
