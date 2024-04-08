class Vector2D:
    """Klasa reprezentująca dwuwymiarowy wektor"""

    def __init__(self, x: float, y: float):
        self.__x, self.__y = float(x), float(y)

    def __str__(self):
        return f"[{self.__x}, {self.__y}]"

    def __repr__(self):
        return f"Vector2D({self.__x}, {self.__y})"

    def __getitem__(self, i: int):
        return [self.__x, self.__y][i]

    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return self.__x == other.__x and self.__y == other.__y
        else:
            return NotImplemented

    def __neg__(self):
        return Vector2D(-self.__x, -self.__y)

    def __add__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.__x + other.__x, self.__y + other.__y)
        elif isinstance(other, tuple) and len(other) == 2:
            return Vector2D(self.__x + float(other[0]), self.__y + float(other[1]))
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            return Vector2D(self.__x + float(other[0]), self.__y + float(other[1]))
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector2D):
            return Vector2D(self.__x - other.__x, self.__y - other.__y)
        elif isinstance(other, tuple) and len(other) == 2:
            return Vector2D(self.__x - other[0], self.__y - other[1])
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, tuple) and len(other) == 2:
            return Vector2D(other[0] - self.__x, other[1] - self.__y)
        else:
            return NotImplemented

    def __mul__(self, other):
        """wektor*wektor = iloczyn skalarny, wektor*liczba = skalar*wektor"""
        if isinstance(other, Vector2D):
            return self.__x * other.__x + self.__y * other.__y
        elif isinstance(other, (int, float)):
            return Vector2D(self.__x * other, self.__y * other)
        elif isinstance(other, tuple) and len(other) == 2:
            return self.__x * float(other[0]) + self.__y * float(other[1])
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2D(self.__x * other, self.__y * other)
        elif isinstance(other, tuple) and len(other) == 2:
            return self.__x * float(other[0]) + self.__y * float(other[1])
        else:
            return NotImplemented
