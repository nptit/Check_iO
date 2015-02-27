def checkio(required, operations):
    total = set()
    hmm = list()
    highest = 0
    lowest = 0
    missing = list()
    for index, op in enumerate(operations, start=1):
        start, stop = op
        if not hmm:  # no need to check multiple tuples for first
            if (stop + 1) - start >= required:
                return index
            hmm.append(op)
            lowest = start
            highest = stop + 1
            # continue  # do i need this? skip because of else??
        else:  # multiple tuples
            if start < lowest:
                lowest = start
            if stop > highest:
                highest = stop
            for pair in hmm:
                lo, hi = pair
                if start > hi:
                    missing.append((hi+1, start-1))
        print(index, missing)


        # # print(list(range(start, stop+1)))
        # # print(set(range(start, stop+1)))
        # total = total.union(set(range(start, stop+1)))
        # # print(total)
        # if len(total) >= required:
        #     return index
        # # print()
    return -1


# print(checkio(5, [[1, 5], [11, 15], [2, 14], [21, 25]]))  # == 1
print(checkio(6, [[1, 5], [11, 15], [2, 14], [21, 25]]))  # == 2
print(checkio(11, [[1, 5], [11, 15], [2, 14], [21, 25]]))  # == 3
# print(checkio(16, [[1, 5], [11, 15], [2, 14], [21, 25]]))  # == 4
# print(checkio(21, [[1, 5], [11, 15], [2, 14], [21, 25]]))  # == -1
# print(checkio(1000000011,[[1, 1000000000],[11, 1000000010]]))  # == -1


# if __name__ == '__main__':
#     assert checkio(5, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 1, "1st"
#     assert checkio(6, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 2, "2nd"
#     assert checkio(11, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 3, "3rd"
#     assert checkio(16, [[1, 5], [11, 15], [2, 14], [21, 25]]) == 4, "4th"
#     assert checkio(21, [[1, 5], [11, 15], [2, 14], [21, 25]]) == -1, "not enough"
#     assert checkio(1000000011, [[1, 1000000000], [11, 1000000010]]) == -1, "large"
