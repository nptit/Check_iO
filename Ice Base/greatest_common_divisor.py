def greatest_common_divisor(*args):
    if type(args[0]) == list or type(args[0]) == tuple:
        args = args[0]
    if len(args) == 2:
        a, b = args[0], args[1]
        while b != 0:
            a, b = b, a % b
        return a
    return greatest_common_divisor(args[0], greatest_common_divisor(args[1:]))

if __name__ == '__main__':
    assert greatest_common_divisor(6, 4) == 2, "Simple"
    assert greatest_common_divisor(2, 4, 8) == 2, "Three arguments"
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1, "Prime numbers"
    assert greatest_common_divisor(3, 9, 3, 9) == 3, "Repeating arguments"
