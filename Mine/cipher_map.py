def recall_password(cipher_grille, ciphered_password):
    cipher_xy = list()
    for a, row in enumerate(cipher_grille):
        [cipher_xy.append((a, dex)) for dex, c in enumerate(row) if c == 'X']

    def clockwise(first, second):
        """
        :param first: X coordinate
        :param second: Y coordinate
        :return: Yield the next coordinate of a given coordinate
                 after rotating clockwise
        """
        for _ in range(4):
            yield (first, second)
            first, second = second, 3 - first

    return ''.join(''.join(ciphered_password[d][e] for d, e in sorted(pairs))
                   for pairs in zip(*(clockwise(*pair) for pair in cipher_xy)))


if __name__ == '__main__':
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
