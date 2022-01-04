

class Utils:

    EPISILON = 1e-6

    @staticmethod
    def isZero(value):
        return abs(value) <= Utils.EPISILON
