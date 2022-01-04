from math import sqrt
from framework.math.utils import Utils


class Vec2(object):

    @staticmethod
    def zero() -> 'Vec2':
        return Vec2(0, 0)

    @staticmethod
    def dot(a: 'Vec2', b: 'Vec2') -> float:
        return a.x * b.x + a.y * b.y

    @staticmethod
    def fromList(l: list) -> 'Vec2':
        assert(len(l) == 2)
        return Vec2(l[0], l[1])

    def __init__(self, x: float = 0, y: float = 0) -> None:
        self.x = x
        self.y = y

    def __add__(self, other: 'Vec2') -> 'Vec2':
        return Vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Vec2') -> 'Vec2':
        return Vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other: 'Vec2') -> 'Vec2':
        return Vec2(self.x * other.x, self.y * other.y)

    def __truediv__(self, other: 'Vec2') -> 'Vec2':
        return Vec2(self.x / other.x, self.y / other.y)

    def __str__(self) -> str:
        return 'Vec2(%f, %f)' % (self.x, self.y)

    def __repr__(self) -> str:
        return 'Vec2(%f, %f)' % (self.x, self.y)

    def __eq__(self, other: 'Vec2') -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other: 'Vec2') -> bool:
        return self.x != other.x or self.y != other.y

    def __neg__(self) -> 'Vec2':
        return Vec2(-self.x, -self.y)

    def scale(self, s: float) -> 'Vec2':
        return Vec2(self.x * s, self.y * s)

    def lengthSqr(self) -> float:
        return self.x * self.x + self.y * self.y

    def length(self) -> float:
        return sqrt(self.lengthSqr())

    def normalize(self) -> 'Vec2':
        l = self.length()
        if Utils.isZero(l):
            return Vec2(0, 0)
        return Vec2(self.x / l, self.y / l)

    def toList(self) -> list:
        return [self.x, self.y]
