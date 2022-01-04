from framework.math.utils import Utils
from math import sqrt


class Vec3:

    @staticmethod
    def zero() -> 'Vec3':
        return Vec3(0, 0, 0)

    @staticmethod
    def fromList(l: list) -> 'Vec3':
        assert(len(l) == 3)
        return Vec3(l[0], l[1], l[2])

    @staticmethod
    def dot(a: 'Vec3', b: 'Vec3') -> float:
        return a.x * b.x + a.y * b.y + a.z * b.z

    @staticmethod
    def cross(a: 'Vec3', b: 'Vec3') -> 'Vec3':
        return Vec3(a.y * b.z - a.z * b.y, a.z * b.x - a.x * b.z, a.x * b.y - a.y * b.x)

    def __init__(self, x: float = 0, y: float = 0, z: float = 0) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other: 'Vec3') -> 'Vec3':
        return Vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: 'Vec3') -> 'Vec3':
        return Vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other: 'Vec3') -> 'Vec3':
        return Vec3(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other: 'Vec3') -> 'Vec3':
        return Vec3(self.x / other.x, self.y / other.y, self.z / other.z)

    def __str__(self) -> str:
        return 'Vec3(%f, %f, %f)' % (self.x, self.y, self.z)

    def __repr__(self) -> str:
        return 'Vec3(%f, %f, %f)' % (self.x, self.y, self.z)

    def __eq__(self, other: 'Vec3') -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __ne__(self, other: 'Vec3') -> bool:
        return self.x != other.x or self.y != other.y or self.z != other.z

    def __neg__(self) -> 'Vec3':
        return Vec3(-self.x, -self.y, -self.z)

    def scale(self, s: float) -> 'Vec3':
        return Vec3(self.x * s, self.y * s, self.z * s)

    def lengthSqr(self) -> float:
        return self.x * self.x + self.y * self.y + self.z * self.z

    def length(self) -> float:
        return sqrt(self.lengthSqr())

    def normalize(self) -> 'Vec3':
        l = self.length()
        if Utils.isZero(l):
            return Vec3(0, 0, 0)
        return self.scale(1.0 / l)

    def toList(self) -> list:
        return [self.x, self.y, self.z]
