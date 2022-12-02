class Figure:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def volume(self):
        return self.a * self.b * self.c


class FigureWithCavity(Figure):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d

    def volume(self):
        return super().volume() - (self.a - self.d) * (self.b - self.d) * (self.c - self.d)


class FigureList(Figure):
    def __init__(self, a, b, c, count):
        super().__init__(a, b, c)
        self.count = count

    def volume(self):
        return super().volume() * self.count
