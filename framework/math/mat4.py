from framework.math.utils import Utils
from framework.math.vec4 import Vec4
from framework.math.vec3 import Vec3


class Mat4:

    @staticmethod
    def makeIdentity() -> 'Mat4':
        return Mat4()

    @staticmethod
    def makeTranslation(x: float, y: float, z: float) -> 'Mat4':
        mat = Mat4()
        mat.m[12] = x
        mat.m[13] = y
        mat.m[14] = z
        return mat

    @staticmethod
    def makeRotation(angle: float, axis: Vec3) -> 'Mat4':
        axis = axis.normalize()
        c = Utils.cos(angle)
        s = Utils.sin(angle)
        t = 1 - c
        x = axis.x
        y = axis.y
        z = axis.z
        return Mat4([
            t * x * x + c, t * x * y - z * s, t * x * z + y * s, 0,
            t * x * y + z * s, t * y * y + c, t * y * z - x * s, 0,
            t * x * z - y * s, t * y * z + x * s, t * z * z + c, 0,
            0, 0, 0, 1
        ])

    @staticmethod
    def makePerspective(fov: float, aspect: float, near: float, far: float) -> 'Mat4':
        f = 1 / Utils.tan(fov / 2)
        return Mat4([
            f / aspect, 0, 0, 0,
            0, f, 0, 0,
            0, 0, (far + near) / (near - far), -1,
            0, 0, (2 * far * near) / (near - far), 0
        ])

    @staticmethod
    def makeScale(x: float, y: float, z: float) -> 'Mat4':
        mat = Mat4()
        mat.m[0] = x
        mat.m[5] = y
        mat.m[10] = z
        return mat

    @staticmethod
    def makeLookAt(eye: Vec3, center: Vec3, up: Vec3) -> 'Mat4':
        f = (center - eye).normalize()
        s = f.cross(up).normalize()
        u = s.cross(f)
        return Mat4([
            s.x, u.x, -f.x, 0,
            s.y, u.y, -f.y, 0,
            s.z, u.z, -f.z, 0,
            0, 0, 0, 1
        ])

    def __init__(self):
        self.m = [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]

    def __getitem__(self, index):
        return self.m[index]

    def __setitem__(self, index, value):
        self.m[index] = value

    def __add__(self, other):
        mat = Mat4()
        for i in range(16):
            mat.m[i] = self.m[i] + other.m[i]
        return mat

    def __sub__(self, other):
        mat = Mat4()
        for i in range(16):
            mat.m[i] = self.m[i] - other.m[i]
        return mat

    def __neg__(self):
        mat = Mat4()
        for i in range(16):
            mat.m[i] = -self.m[i]
        return mat

    def __mul__(self, other: 'Mat4'):
        mat = Mat4()
        mat.m[0] = self.m[0] * other.m[0] + self.m[4] * other.m[1] + \
            self.m[8] * other.m[2] + self.m[12] * other.m[3]
        mat.m[1] = self.m[1] * other.m[0] + self.m[5] * other.m[1] + \
            self.m[9] * other.m[2] + self.m[13] * other.m[3]
        mat.m[2] = self.m[2] * other.m[0] + self.m[6] * other.m[1] + \
            self.m[10] * other.m[2] + self.m[14] * other.m[3]
        mat.m[3] = self.m[3] * other.m[0] + self.m[7] * other.m[1] + \
            self.m[11] * other.m[2] + self.m[15] * other.m[3]
        mat.m[4] = self.m[0] * other.m[4] + self.m[4] * other.m[5] + \
            self.m[8] * other.m[6] + self.m[12] * other.m[7]
        mat.m[5] = self.m[1] * other.m[4] + self.m[5] * other.m[5] + \
            self.m[9] * other.m[6] + self.m[13] * other.m[7]
        mat.m[6] = self.m[2] * other.m[4] + self.m[6] * other.m[5] + \
            self.m[10] * other.m[6] + self.m[14] * other.m[7]
        mat.m[7] = self.m[3] * other.m[4] + self.m[7] * other.m[5] + \
            self.m[11] * other.m[6] + self.m[15] * other.m[7]
        mat.m[8] = self.m[0] * other.m[8] + self.m[4] * other.m[9] + \
            self.m[8] * other.m[10] + self.m[12] * other.m[11]
        mat.m[9] = self.m[1] * other.m[8] + self.m[5] * other.m[9] + \
            self.m[9] * other.m[10] + self.m[13] * other.m[11]
        mat.m[10] = self.m[2] * other.m[8] + self.m[6] * other.m[9] + \
            self.m[10] * other.m[10] + self.m[14] * other.m[11]
        mat.m[11] = self.m[3] * other.m[8] + self.m[7] * other.m[9] + \
            self.m[11] * other.m[10] + self.m[15] * other.m[11]
        mat.m[12] = self.m[0] * other.m[12] + self.m[4] * other.m[13] + \
            self.m[8] * other.m[14] + self.m[12] * other.m[15]
        mat.m[13] = self.m[1] * other.m[12] + self.m[5] * other.m[13] + \
            self.m[9] * other.m[14] + self.m[13] * other.m[15]
        mat.m[14] = self.m[2] * other.m[12] + self.m[6] * other.m[13] + \
            self.m[10] * other.m[14] + self.m[14] * other.m[15]
        mat.m[15] = self.m[3] * other.m[12] + self.m[7] * other.m[13] + \
            self.m[11] * other.m[14] + self.m[15] * other.m[15]
        return mat

    def __str__(self):
        return '\n'.join([' '.join(map(str, self.m[i:i+4])) for i in range(0, 16, 4)])

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        for i in range(16):
            if self.m[i] != other.m[i]:
                return False
        return True

    def __ne__(self, other):
        return not self == other

    def multiplyVec4(self, vec: 'Vec4') -> 'Vec4':
        return Vec4(
            self.m[0] * vec.x + self.m[4] * vec.y +
            self.m[8] * vec.z + self.m[12] * vec.w,
            self.m[1] * vec.x + self.m[5] * vec.y +
            self.m[9] * vec.z + self.m[13] * vec.w,
            self.m[2] * vec.x + self.m[6] * vec.y +
            self.m[10] * vec.z + self.m[14] * vec.w,
            self.m[3] * vec.x + self.m[7] * vec.y +
            self.m[11] * vec.z + self.m[15] * vec.w
        )

    def scale(self, s: float) -> 'Mat4':
        mat = Mat4()
        mat.m[0] = self.m[0] * s
        mat.m[1] = self.m[1] * s
        mat.m[2] = self.m[2] * s
        mat.m[3] = self.m[3] * s
        mat.m[4] = self.m[4] * s
        mat.m[5] = self.m[5] * s
        mat.m[6] = self.m[6] * s
        mat.m[7] = self.m[7] * s
        mat.m[8] = self.m[8] * s
        mat.m[9] = self.m[9] * s
        mat.m[10] = self.m[10] * s
        mat.m[11] = self.m[11] * s
        mat.m[12] = self.m[12] * s
        mat.m[13] = self.m[13] * s
        mat.m[14] = self.m[14] * s
        mat.m[15] = self.m[15] * s
        return mat

    def transpose(self):
        mat = Mat4()
        mat.m[0] = self.m[0]
        mat.m[1] = self.m[4]
        mat.m[2] = self.m[8]
        mat.m[3] = self.m[12]
        mat.m[4] = self.m[1]
        mat.m[5] = self.m[5]
        mat.m[6] = self.m[9]
        mat.m[7] = self.m[13]
        mat.m[8] = self.m[2]
        mat.m[9] = self.m[6]
        mat.m[10] = self.m[10]
        mat.m[11] = self.m[14]
        mat.m[12] = self.m[3]
        mat.m[13] = self.m[7]
        mat.m[14] = self.m[11]
        mat.m[15] = self.m[15]
        return mat

    def inverse(self):

        # shamelessly copied from https://github.com/toji/gl-matrix/blob/master/src/mat4.js
        a00 = self.m[0]
        a01 = self.m[1]
        a02 = self.m[2]
        a03 = self.m[3]
        a10 = self.m[4]
        a11 = self.m[5]
        a12 = self.m[6]
        a13 = self.m[7]
        a20 = self.m[8]
        a21 = self.m[9]
        a22 = self.m[10]
        a23 = self.m[11]
        a30 = self.m[12]
        a31 = self.m[13]
        a32 = self.m[14]
        a33 = self.m[15]

        b00 = a00 * a11 - a01 * a10
        b01 = a00 * a12 - a02 * a10
        b02 = a00 * a13 - a03 * a10
        b03 = a01 * a12 - a02 * a11
        b04 = a01 * a13 - a03 * a11
        b05 = a02 * a13 - a03 * a12
        b06 = a20 * a31 - a21 * a30
        b07 = a20 * a32 - a22 * a30
        b08 = a20 * a33 - a23 * a30
        b09 = a21 * a32 - a22 * a31
        b10 = a21 * a33 - a23 * a31
        b11 = a22 * a33 - a23 * a32

        det = b00 * b11 - b01 * b10 + b02 * b09 + b03 * b08 - b04 * b07 + b05 * b06

        if Utils.isZero(det):
            return None

        det = 1.0 / det
        out = Mat4()
        out.m[0] = (a11 * b11 - a12 * b10 + a13 * b09) * det
        out.m[1] = (a02 * b10 - a01 * b11 - a03 * b09) * det
        out.m[2] = (a31 * b05 - a32 * b04 + a33 * b03) * det
        out.m[3] = (a22 * b04 - a21 * b05 - a23 * b03) * det
        out.m[4] = (a12 * b08 - a10 * b11 - a13 * b07) * det
        out.m[5] = (a00 * b11 - a02 * b08 + a03 * b07) * det
        out.m[6] = (a32 * b02 - a30 * b05 - a33 * b01) * det
        out.m[7] = (a20 * b05 - a22 * b02 + a23 * b01) * det
        out.m[8] = (a10 * b10 - a11 * b08 + a13 * b06) * det
        out.m[9] = (a01 * b08 - a00 * b10 - a03 * b06) * det
        out.m[10] = (a30 * b04 - a31 * b02 + a33 * b00) * det
        out.m[11] = (a21 * b02 - a20 * b04 - a23 * b00) * det
        out.m[12] = (a11 * b07 - a10 * b09 - a12 * b06) * det
        out.m[13] = (a00 * b09 - a01 * b07 + a02 * b06) * det
        out.m[14] = (a31 * b01 - a30 * b03 - a32 * b00) * det
        out.m[15] = (a20 * b03 - a21 * b01 + a22 * b00) * det
        return out
