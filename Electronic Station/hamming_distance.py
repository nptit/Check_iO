from itertools import zip_longest


def checkio(n, m):
    return sum(1 for a, b in zip_longest(reversed('{:b}'.format(n)),
                                         reversed('{:b}'.format(m)),
                                         fillvalue='0') if not a == b)

if __name__ == '__main__':
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
    assert checkio(1, 999999) == 11, 'Fourth example'
