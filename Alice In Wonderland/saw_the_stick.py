def triangle_numbers(limit):
    cnt = 1
    while True:
        tri_num = int((cnt / 2) * (cnt + 1))
        if tri_num >= limit:
            break
        yield tri_num
        cnt += 1


def checkio(number):
    tri_nums = list(triangle_numbers(number))
    highest = list()  # stays as an empty list in case of no match below
    for a in range(1, len(tri_nums) + 1):
        for b in range(len(tri_nums) - (a - 1)):
            curr = tri_nums[b:b+a]
            total = sum(curr)
            if total == number:
                highest = curr
            elif total > number:
                break
    return highest

if __name__ == '__main__':
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
    assert checkio(10) == [1, 3, 6]
