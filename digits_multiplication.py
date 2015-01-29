from functools import reduce


def checkio(nums):
    return reduce(lambda b, c: b * c, (int(a) for a in str(nums) if not a == '0'))

# def checkio(nums):
#     total = 1
#     for b in (int(a) for a in str(nums) if not a == '0'):
#         total *= b
#     return total

if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
