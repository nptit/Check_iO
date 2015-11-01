def seconds_to_hms(seconds):
    h, mins = divmod(seconds, 3600)
    m, s = divmod(mins, 60)
    return '{:0>2}:{:0>2}:{:0>2}'.format(h, m, s)


def to_seconds(time, t_value=None):
    if isinstance(time, str):
        return sum(int(a) * b for a, b in zip(time.split(':'), (3600, 60, 1)))
    if t_value.startswith('second'):
        return time
    elif t_value.startswith('minute'):
        return time * 60
    return time * 3600


def broken_clock(starting_time, wrong_time, error_description):
    uno, uno_val, dos, dos_val = error_description.replace('at', '').split()
    uno = to_seconds(int(uno), uno_val)
    dos = to_seconds(int(dos), dos_val)
    start_seconds = to_seconds(starting_time)
    diff = abs(start_seconds - to_seconds(wrong_time))
    return seconds_to_hms(start_seconds + int((dos / (uno + dos)) * diff))

if __name__ == "__main__":
    assert broken_clock('00:00:00', '00:00:15', '+5 seconds at 10 seconds') \
        == '00:00:10', "First example"
    assert broken_clock('06:10:00', '06:10:15', '-5 seconds at 10 seconds') \
        == '06:10:30', 'Second example'
    assert broken_clock('13:00:00', '14:01:00', '+1 second at 1 minute') \
        == '14:00:00', 'Third example'
    assert broken_clock('01:05:05', '04:05:05', '-1 hour at 2 hours') \
        == '07:05:05', 'Fourth example'
    assert broken_clock('00:00:00', '00:00:30', '+2 seconds at 6 seconds') \
        == '00:00:22', 'Fifth example'
