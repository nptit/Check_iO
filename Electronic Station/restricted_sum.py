def checkio(num):
    return 0 if not num else num[0] + checkio(num[1:])

assert checkio([1, 2, 3]) == 6
