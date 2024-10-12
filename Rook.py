# move
# position


class Rook:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f"The position of Rook is{self.x}, {self.y}")

    def get_position(self):
        return self.x, self.y