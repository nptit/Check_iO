def recognize(n):
    return len(set(a for a in bin(n)[2:].split('0')if a))==1

if __name__ == '__main__':
    assert recognize(21) is True, "First example"
    assert recognize(1587) is True, "Second example"
    assert recognize(3687) is False, "Third example"

'''
This is a code golf mission and your main goal is to make your code
as short as possible. The shorter your code, the more points you earn.
Your score for this mission is dynamic and directly related to the
length of your code. For reference, scoring is based on the number of
characters used. 200 characters is the maximum allowable and it will
earn you zero points. For each character less than 220, you earn 1 point.
For example for 150 character long code earns you 50 points. In this
mission we count whitespaces, but don't count indents.
'''
