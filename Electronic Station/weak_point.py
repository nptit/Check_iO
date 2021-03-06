def lowest_index(lst):
    min_index = None
    lowest = None
    for index, horizontal in enumerate(lst):
        current = sum(horizontal)
        if min_index is None or lowest is None or current < lowest:
            min_index = index
            lowest = current
    return min_index


def weak_point(matrix):
    return [lowest_index(matrix), lowest_index(zip(*matrix))]


if __name__ == '__main__':
    assert isinstance(weak_point([[1]]), (list, tuple))
    assert list(weak_point([[7, 2, 7, 2, 8],
                            [2, 9, 4, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [3, 3]
    assert list(weak_point([[7, 2, 4, 2, 8],
                            [2, 8, 1, 1, 7],
                            [3, 8, 6, 2, 4],
                            [2, 5, 2, 9, 1],
                            [6, 6, 5, 4, 5]])) == [1, 2]
    assert list(weak_point([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])) == [0, 0]
