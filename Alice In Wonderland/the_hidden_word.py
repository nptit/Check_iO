from itertools import zip_longest


def checkio(text, word):
    def result(start, line_num, horizontal=True):
        if horizontal:
            return [line_num, start + 1, line_num, start + len(word)]
        return [start + 1, line_num, start + len(word), line_num]

    horizontal = list()
    for dex, line in enumerate(text.split('\n')):
        curr = ''.join(line.split()).lower()
        horizontal.append(curr)
        if word in curr:
            return result(curr.find(word), dex + 1)

    for dex, line in enumerate(zip_longest(*horizontal, fillvalue='*')):
        curr = ''.join(line).lower()
        if word in curr:
            return result(curr.find(word), dex + 1, horizontal=False)

if __name__ == '__main__':
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]
