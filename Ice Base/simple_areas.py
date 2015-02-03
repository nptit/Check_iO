from math import pi, sqrt


def simple_areas(*args):
    total_args = len(args)
    if total_args == 1:    # circle
        return round(pi * (args[0]/2)**2, 2)
    elif total_args == 2:  # square / rectangle
        return round(args[0] * args[1], 2)
    elif total_args == 3:  # triangle
        s = (args[0] + args[1] + args[2]) / 2
        return round(sqrt(s * (s - args[0]) * (s - args[1]) * (s - args[2])), 2)

if __name__ == '__main__':
    def almost_equal(checked, correct, significant_digits=2):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(simple_areas(3), 7.07), "Circle"
    assert almost_equal(simple_areas(2, 2), 4), "Square"
    assert almost_equal(simple_areas(2, 3), 6), "Rectangle"
    assert almost_equal(simple_areas(3, 5, 4), 6), "Triangle"
    assert almost_equal(simple_areas(1.5, 2.5, 2), 1.5), "Small triangle"
