from fractions import Fraction


def divide_pie(groups):
    total_drones = sum(abs(a) for a in groups)
    fraction = {abs(b): Fraction(abs(b), total_drones) for b in groups}
    pie_left = Fraction(1)
    for c in groups:
        if c < 0:
            pie_left -= pie_left * fraction[abs(c)]
        else:
            pie_left -= Fraction(1, 1) * fraction[abs(c)]
    return pie_left.numerator, pie_left.denominator

if __name__ == '__main__':
    assert isinstance((2, -2), (tuple, list)), "Return tuple or list"
    assert tuple(divide_pie((2, -1, 3))) == (1, 18), "Example"
    assert tuple(divide_pie((1, 2, 3))) == (0, 1), "All know about the pie"
    assert tuple(divide_pie((-1, -1, -1))) == (8, 27), "One by one"
    assert tuple(divide_pie((10,))) == (0, 1), "All together"
