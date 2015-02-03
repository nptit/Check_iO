def create_key_table(key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
    key_dict = dict()     # key = character, value = (x, y) char coordinates
    key_letters = list()

    [key_letters.append(a) for a in key + alphabet if a not in key_letters]
    key_table = [key_letters[b:b+6] for b in range(0, 36, 6)]

    for x, row in enumerate(key_table):
        for y, char in enumerate(row):
            key_dict[char] = (x, y)
    return key_table, key_dict


def encode(message, key):
    msg = ''.join(a.lower() for a in message if a.isalnum())
    msg_len = len(msg)                  # message text normalized
    digraph = list()                    # all 2 character chunks
    di = list()                         # single 2 character chunk
    for dex, curr in enumerate(msg):
        di_length = len(di)
        if di_length == 0:
            di.append(curr)
            if dex == msg_len - 1:      # last character, needs completion
                di.append('x' if curr == 'z' else 'z')
        elif di_length == 1:
            if di[0] == curr:
                com_char = 'z' if curr == 'x' else 'x'  # completion character
                di.append(com_char)
                digraph.append(''.join(di))
                if dex == msg_len - 1:  # last character, needs completion
                    di = [curr, com_char]
                else:
                    di = [curr]         # not last character, grab next in msg
            else:
                di.append(curr)         # characters are different

        if len(di) == 2:                # check if new length is 2
            digraph.append(''.join(di))
            di = list()

    key_table, key_dict = create_key_table(key)
    cipher = list()
    for uno, dos in digraph:
        x1, y1 = key_dict[uno]
        x2, y2 = key_dict[dos]
        if x1 == x2:    # same row
            cipher.append(key_table[x1][y1 + 1 if not y1 == 5 else 0])
            cipher.append(key_table[x2][y2 + 1 if not y2 == 5 else 0])
        elif y1 == y2:  # same column
            cipher.append(key_table[x1 + 1 if not x1 == 5 else 0][y1])
            cipher.append(key_table[x2 + 1 if not x2 == 5 else 0][y2])
        else:
            cipher.append(key_table[x1][y2])
            cipher.append(key_table[x2][y1])
    return ''.join(cipher)


def decode(cipher, key):
    key_table, key_dict = create_key_table(key)
    plain = list()
    for uno, dos in(cipher[a:a+2] for a in range(0, len(cipher), 2)):
        x1, y1 = key_dict[uno]
        x2, y2 = key_dict[dos]
        if x1 == x2:    # same row
            plain.append(key_table[x1][y1 - 1 if not y1 == 0 else 5])
            plain.append(key_table[x2][y2 - 1 if not y2 == 0 else 5])
        elif y1 == y2:  # same column
            plain.append(key_table[x1 - 1 if not x1 == 0 else 5][y1])
            plain.append(key_table[x2 - 1 if not x2 == 0 else 5][y2])
        else:
            plain.append(key_table[x1][y2])
            plain.append(key_table[x2][y1])
    return ''.join(plain)

if __name__ == '__main__':
    assert encode("Fizz Buzz is x89 XX.", "checkio101") == 'do2y7mt22kry94y2y2', "Encode fizz buzz"
    assert decode("do2y7mt22kry94y2y2", "checkio101") == 'fizxzbuzzisx89xzxz', "Decode fizz buzz"
    assert encode("How are you?", "hello") == 'ea2imb1ht0', "Encode How are you"
    assert decode("ea2imb1ht0", "hello") == 'howareyouz', "Decode How are you"
    assert encode("My name is Alex!!!", "alexander") == 'i1dlkxjqlexn', "Encode Alex"
    assert decode("i1dlkxjqlexn", "alexander") == 'mynameisalex', "Decode Alex"
    assert encode("Who are you?", "human") == 'rnvftc1jd5', "Encode WHo"
    assert decode("rnvftc1jd5", "human") == 'whoareyouz', "Decode Who"
    assert encode("ATTACK AT DAWN", "general") == 'ewwektewhnua', "Encode attack"
    assert decode("ewwektewhnua", "general") == 'attackatdawn', "Decode attack"
