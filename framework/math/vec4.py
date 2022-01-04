from framework.math.utils import Utils
from math import sqrt


class Vec4:

    @staticmethod
    def fromList(l: list) -> 'Vec4':
        assert(len(l) == 4)
        return Vec4(l[0], l[1], l[2], l[3])

    @staticmethod
    def dot(a: 'Vec4', b: 'Vec4') -> float:
        return a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w

    @staticmethod
    def zero() -> 'Vec4':
        return Vec4(0, 0, 0, 0)

    # @staticmethod
    # def cross(a: 'Vec4', b: 'Vec4') -> 'Vec4':
    #     return Vec4(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x, 0)

    def __init__(self, x: float = 0, y: float = 0, z: float = 0, w: float = 0) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __add__(self, other: 'Vec4') -> 'Vec4':
        return Vec4(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def __sub__(self, other: 'Vec4') -> 'Vec4':
        return Vec4(self.x - other.x, self.y - other.y, self.z - other.z, self.w - other.w)

    def __mul__(self, other: 'Vec4') -> 'Vec4':
        return Vec4(self.x * other.x, self.y * other.y, self.z * other.z, self.w * other.w)

    def __truediv__(self, other: 'Vec4') -> 'Vec4':
        return Vec4(self.x / other.x, self.y / other.y, self.z / other.z, self.w / other.w)

    def __str__(self) -> str:
        return 'Vec4(%f, %f, %f, %f)' % (self.x, self.y, self.z, self.w)

    def __repr__(self) -> str:
        return 'Vec4(%f, %f, %f, %f)' % (self.x, self.y, self.z, self.w)

    def __eq__(self, other: 'Vec4') -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z and self.w == other.w

    def __ne__(self, other: 'Vec4') -> bool:
        return self.x != other.x or self.y != other.y or self.z != other.z or self.w != other.w

    def __neg__(self) -> 'Vec4':
        return Vec4(-self.x, -self.y, -self.z, -self.w)

    def scale(self, s: float) -> 'Vec4':
        return Vec4(self.x * s, self.y * s, self.z * s, self.w * s)

    def lengthSqr(self) -> float:
        return self.x * self.x + self.y * self.y + self.z * self.z + self.w * self.w

    def length(self) -> float:
        return sqrt(self.lengthSqr())

    def normalize(self) -> 'Vec4':
        length = self.length()
        if Utils.isZero(length):
            return Vec4(0, 0, 0, 0)
        return Vec4(self.x / length, self.y / length, self.z / length, self.w / length)

    def toList(self) -> list:
        return [self.x, self.y, self.z, self.w]
