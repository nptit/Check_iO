from collections import deque


def checkio(txt):
    open_brackets, close_brackets = '[{(', ']})'
    for i, a in enumerate(open_brackets):
        if not txt.count(a) == txt.count(close_brackets[i]):
            return False

    deq = deque()
    for b in txt:
        if b in close_brackets:
            zero = deq.popleft()
            if not zero == open_brackets[close_brackets.index(b)]:
                return False
        elif b in open_brackets:
            deq.appendleft(b)
    return True

if __name__ == '__main__':
    assert checkio("((5+3)*2+1)") == True, "Simple"
    assert checkio("{[(3+1)+2]+}") == True, "Different types"
    assert checkio("(3+{1-1)}") == False, ") is alone inside {}"
    assert checkio("[1+1]+(2*2)-{3/3}") == True, "Different operators"
    assert checkio("(({[(((1)-2)+3)-3]/3}-3)") == False, "One is redundant"
    assert checkio("2+3") == True, "No brackets, no problem"
