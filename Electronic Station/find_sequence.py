def checkio(matrix):
    for row in matrix:           # horizontal
        if chunk_checker(''.join(str(a) for a in row)):
            return True
    for column in zip(*matrix):  # vertical
        if chunk_checker(''.join(str(b) for b in column)):
            return True
    if diagonal(matrix):         # diagonal
        return True
    return diagonal([c[::-1] for c in matrix])  # reverse the list


def chunk_checker(txt):
    if len(txt) >= 4:
        for num in set(txt):
            if num * 4 in txt:
                return True
    return False


def diagonal(lst):
    height = len(lst)
    width = len(lst[0])
    for d in range(height):
        nw_se = list()
        curr_x = d
        for e in range(width):  # NW - SE
            if curr_x >= height:
                break
            nw_se.append(str(lst[curr_x][e]))
            curr_x += 1
        if chunk_checker(''.join(nw_se)):
            return True

        sw_ne = list()
        curr_x = d
        for f in range(width):  # SW - NE
            if curr_x < 0:
                break
            sw_ne.append(str(lst[curr_x][f]))
            curr_x -= 1
        if chunk_checker(''.join(sw_ne)):
            return True
    return False


print(checkio([[1, 2, 1, 1],
               [1, 1, 4, 1],
               [1, 3, 1, 6],
               [1, 7, 2, 5]]))

print(checkio([[7, 1, 4, 1],
               [1, 2, 5, 2],
               [3, 4, 1, 3],
               [1, 1, 8, 1]]))

print(checkio([[2, 1, 1, 6, 1],
               [1, 3, 2, 1, 1],
               [4, 1, 1, 3, 1],
               [5, 5, 5, 5, 5],
               [1, 1, 3, 1, 1]]))

print(checkio([[7, 1, 1, 8, 1, 1],
               [1, 1, 7, 3, 1, 5],
               [2, 3, 1, 2, 5, 1],
               [1, 1, 1, 5, 1, 4],
               [4, 6, 5, 1, 3, 1],
               [1, 1, 9, 1, 2, 1]]))
