def time_to_morse(nums, lengths):
    left, right = nums
    l_len, r_len = lengths
    return ' '.join((binary_to_morse('{:0>{}b}'.format(left, l_len)),
                     binary_to_morse('{:0>{}b}'.format(right, r_len))))


def binary_to_morse(binary):
    return ''.join('.' if a == '0' else '-' for a in binary)


def checkio(time_str):
    h, m, s = (tuple(int(b) for b in a.zfill(2)) for a in time_str.split(':'))
    return ' : '.join((time_to_morse(h, (2, 4)),
                       time_to_morse(m, (3, 4)),
                       time_to_morse(s, (3, 4))))

if __name__ == '__main__':
    assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
    assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
    assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
    assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
