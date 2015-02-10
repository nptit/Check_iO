from itertools import zip_longest


def check_command(pattern, command):
    for a, b in zip_longest(reversed('{:b}'.format(pattern)),
                            command[::-1], fillvalue='0'):
        if a == '0' and not b.isdigit() or a == '1' and not b.isalpha():
            return False
    return True

if __name__ == '__main__':
    assert check_command(42, "12a0b3e4") is True, "42 is the answer"
    assert check_command(101, "ab23b4zz") is False, "one hundred plus one"
    assert check_command(0, "478103487120470129") is True, "Any number"
    assert check_command(127, "Checkio") is True, "Uppercase"
    assert check_command(7, "Hello") is False, "Only full match"
    assert check_command(8, "a") is False, "Too short command"
    assert check_command(5, "H2O") is True, "Water"
    assert check_command(42, "C2H5OH") is False, "Yep, this is not the Answer"
