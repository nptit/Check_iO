from math import acos, degrees


def angle(a, b, c):
    """ Returns angle, in degrees and rounded, for one corner of a triangle """
    return round(degrees(acos((a*a + b*b - c*c) / (2*a*b))))


def checkio(a, b, c):
    """ Returns [0, 0, 0] to indicate invalid triangle side lengths.
        Any two sides added together should be greater than the third.
        Otherwise, calculates all three internal angles of the triangle. """
    if not a + b > c:
        return [0, 0, 0]
    angle_1 = angle(a, b, c)
    angle_2 = angle(b, c, a)
    return sorted([angle_1, angle_2, round(180 - angle_1 - angle_2)])

if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
