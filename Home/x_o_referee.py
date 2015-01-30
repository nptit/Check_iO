def checkio(lst):
    ooo, xxx = {'O'}, {'X'}
    for a in lst:                              # horizontal rows
        horizontal = set(a)
        if horizontal == xxx:
            return 'X'
        elif horizontal == ooo:
            return 'O'
    for b in zip(*lst):                        # vertical columns
        vertical = set(b)
        if vertical == xxx:
            return 'X'
        elif vertical == ooo:
            return 'O'
    diag = {lst[0][0], lst[1][1], lst[2][2]}   # top-left to bottom-right
    diag2 = {lst[0][2], lst[1][1], lst[2][0]}  # bottom-left to top-right
    if diag == xxx or diag2 == xxx:
        return 'X'
    elif diag == ooo or diag2 == ooo:
        return 'O'
    return 'D'

if __name__ == '__main__':
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
