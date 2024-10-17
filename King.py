# move
# position


class King:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True

    def display(self):
        print(f"The position of King is{self.x}, {self.y}")

    def get_position(self):
        return self.x, self.y
    
    def is_alive(self):
        return self.alive
    
    def kill(self):
        self.alive = False
        print("King is dead, game ended")
