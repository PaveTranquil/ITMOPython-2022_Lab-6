class Figure:
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def volume(self):
        return self.a * self.b * self.c

    def __add__(self, other):
        if isinstance(other, FigureWithCavity):
            return FigureWithCavity(self.a + other.a, self.b + other.b, self.c + other.c, other.d)
        if isinstance(other, FigureList) and (self.a, self.b, self.c) == (other.a, other.b, other.c):
            return FigureList(self.a, self.b, self.c, other.count + 1)
        if isinstance(other, Figure):
            return Figure(self.a + other.a, self.b + other.b, self.c + other.c)
        return self.volume() + other.volume()


class FigureWithCavity(Figure):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d

    def volume(self):
        return super().volume() - (self.a - self.d) * (self.b - self.d) * (self.c - self.d)

    def __add__(self, other):
        if isinstance(other, Figure):
            return FigureWithCavity(self.a + other.a, self.b + other.b, self.c + other.c, self.d)
        if isinstance(other, FigureWithCavity):
            return FigureWithCavity(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)
        if isinstance(other, FigureList) and (self.a, self.b, self.c) == (other.a, other.b, other.c):
            raise ValueError("Нельзя прибавлять фигуру с пустотой к массиву обычных фигур")
        return self.volume() + other.volume()


class FigureList(Figure):
    def __init__(self, a, b, c, count):
        super().__init__(a, b, c)
        self.count = count

    def volume(self):
        return super().volume() * self.count

    def __add__(self, other):
        if isinstance(other, FigureList) and (self.a, self.b, self.c) == (other.a, other.b, other.c):
            return FigureList(self.a, self.b, self.c, self.count + other.count)
        if isinstance(other, Figure) and (self.a, self.b, self.c) == (other.a, other.b, other.c):
            return FigureList(self.a, self.b, self.c, self.count + 1)
        if isinstance(other, FigureWithCavity):
            raise ValueError('Нельзя прибавлять к массиву обычных фигур фигуры с пустотой')
        return self.volume() + other.volume()
