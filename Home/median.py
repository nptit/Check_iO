def checkio(lst):
    length = len(lst)
    lst = sorted(lst)
    if length % 2 == 0:
        mid = int(length / 2)
        return (lst[mid] + lst[mid-1]) / 2
    return lst[int(length / 2)]

if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")
