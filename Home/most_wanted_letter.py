def checkio(s):
    lower = [a.lower() for a in s if a.isalpha()]
    counts = dict()
    for letter in set(lower):
        cnt = lower.count(letter)
        if cnt not in counts:
            counts[cnt] = list()
        counts[cnt].append(letter)
    return sorted(counts[max(counts)])[0]

if __name__ == '__main__':
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")

# # my old way... ?? better/worse?
# from itertools import groupby
# 
# def checkio(s):
#     str = ''.join(sorted([x.lower() for x in s if x.isalpha()]))
#     b = [list(y) for x, y in groupby(str)]
#     l = [len(x) for x in b]
#     return next(b[i][0] for i, x in enumerate(l) if x == max(l))
