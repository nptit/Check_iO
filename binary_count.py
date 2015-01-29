def checkio(n): 
    """ 1000000 loops, best of 3: 1.5 µs per loop """
    return bin(n).count('1')

# def checkio(n):
#     """ 100000 loops, best of 3: 5.22 µs per loop """
#     return sum(1 for a in bin(n) if a == '1')

if __name__ == '__main__':
    assert checkio(4) == 1
    assert checkio(15) == 4
    assert checkio(1) == 1
    assert checkio(1022) == 9
