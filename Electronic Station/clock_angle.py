def clock_angle(time):
    hour, mins = (int(a) for a in time.split(':'))
    hour = hour - 12 if hour >= 12 else hour
    angle = abs(((hour * 30) + (mins * 0.5)) - (mins * 6))
    str_angle = '{:.2f}'.format(angle if angle < 180 else 360 - angle)
    try:
        return 0 if not str_angle else int(str_angle.rstrip('0').rstrip('.'))
    except ValueError:
        return float(str_angle.rstrip('0').rstrip('.'))  # float

if __name__ == '__main__':
    assert clock_angle("02:30") == 105
    assert clock_angle("13:42") == 159
    assert clock_angle("01:42") == 159
    assert clock_angle("01:43") == 153.5
    assert clock_angle("00:00") == 0
    assert clock_angle("12:01") == 5.5
    assert clock_angle("18:00") == 180
