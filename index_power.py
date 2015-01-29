def index_power(array, n):
    """ Find nth power of the element with index n """
    if n > len(array) - 1:
        return -1
    return array[n] ** n

if __name__ == '__main__':
    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 2], 3) == -1, "IndexError"
