from datetime import date


def days_diff(date1, date2):
    """ Find absolute diff in days between dates """
    y, m, d = date1
    y2, m2, d2 = date2
    return abs((date(y, m, d) - date(y2, m2, d2)).days)

if __name__ == '__main__':
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
