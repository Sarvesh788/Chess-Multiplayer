class Bishop:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def display(self):
        print(f"The position of Bishop is{self.x}, {self.y}")

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x, self.y  
