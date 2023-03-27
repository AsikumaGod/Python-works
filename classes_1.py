class Trial:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        def __add__(self):
            return Trial(self.x + self.y)

        point = Trial(4, 5)
