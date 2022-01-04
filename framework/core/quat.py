from math import sqrt, sin, cos
from framework.core.matrix import Matrix


class Quat(object):

    @staticmethod
    def dot(a, b):
        return a.x * b.x + a.y * b.y + a.z * b.z + a.w * b.w

    @staticmethod
    def fromAxisAngle(axis, angle):
        s = sin(angle / 2)
        c = cos(angle / 2)
        return Quat(axis.x * s, axis.y * s, axis.z * s, c)

    @staticmethod
    def fromMat4(mat):
        m = mat.toList()
        t = m[0] + m[5] + m[10] + 1
        if t > 0:
            s = 0.5 / sqrt(t)
            w = 0.25 / s
            x = (m[6] - m[9]) * s
            y = (m[8] - m[2]) * s
            z = (m[1] - m[4]) * s
        elif m[0] > m[5] and m[0] > m[10]:
            s = 2 * sqrt(1 + m[0] - m[5] - m[10])
            w = (m[6] - m[9]) / s
            x = 0.25 * s
            y = (m[1] + m[4]) / s
            z = (m[8] + m[2]) / s
        elif m[5] > m[10]:
            s = 2 * sqrt(1 + m[5] - m[0] - m[10])
            w = (m[8] - m[2]) / s
            x = (m[1] + m[4]) / s
            y = 0.25 * s
            z = (m[6] + m[9]) / s
        else:
            s = 2 * sqrt(1 + m[10] - m[0] - m[5])
            w = (m[1] - m[4]) / s
            x = (m[8] + m[2]) / s
            y = (m[6] + m[9]) / s
            z = 0.25 * s
        return Quat(x, y, z, w)

    def __init__(self, x=0, y=0, z=0, w=1):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __add__(self, other):
        return Quat(self.x + other.x, self.y + other.y, self.z + other.z, self.w + other.w)

    def length(self):
        return sqrt(self.x * self.x + self.y * self.y + self.z * self.z + self.w * self.w)

    def toMat4(self):
        xx = self.x * self.x
        xy = self.x * self.y
        xz = self.x * self.z
        xw = self.x * self.w
        yy = self.y * self.y
        yz = self.y * self.z
        yw = self.y * self.w
        zz = self.z * self.z
        zw = self.z * self.w
        return Matrix.make([1 - 2 * (yy + zz), 2 * (xy + zw), 2 * (xz - yw), 0,
                            2 * (xy - zw), 1 - 2 * (xx + zz), 2 * (yz + xw), 0,
                            2 * (xz + yw), 2 * (yz - xw), 1 - 2 * (xx + yy), 0,
                            0, 0, 0, 1])
