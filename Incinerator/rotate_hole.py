def rotate(state, pipe_numbers):
    dex = 0
    length = len(state)
    results = list()
    for a in range(length, 0, -1):
        tmp = list()
        for b in range(length):
            tmp.append(state[(a+b) % length])
        pipe_match = True
        for num in pipe_numbers:
            if tmp[num] == 0:
                pipe_match = False
                break
        if pipe_match:
            results.append(dex)
        dex += 1
    return results

if __name__ == '__main__':
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1]) == [1, 8]
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 1], [0, 1, 2]) == []
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [0, 4, 5]) == [0]
    assert rotate([1, 0, 0, 0, 1, 1, 0, 1], [5, 4, 5]) == [0, 5]
