def clean_keyword(keyword):
    key = list()
    [key.append(a.lower()) for a in keyword if a.isalnum() and a not in key]
    return ''.join(key)


def create_table(alphabet, to_encode=True):
    adfgvx = {b: c for b, c in zip(range(6), 'ADFGVX')}
    dex = 0
    table_dict = dict()
    for d in range(6):
        for e in range(6):
            if to_encode:  # for encoding
                table_dict[alphabet[dex]] = ''.join((adfgvx[d], adfgvx[e]))
            else:          # for decoding
                table_dict[''.join((adfgvx[d], adfgvx[e]))] = alphabet[dex]
            dex += 1
    return table_dict


def encode(message, secret_alphabet, keyword):
    msg = ''.join(a.lower() for a in message if a.isalnum())
    adfgvx_table = create_table(secret_alphabet)
    fractionated = ''.join(adfgvx_table[char] for char in msg)  # wrong name?
    keyword = clean_keyword(keyword)
    dex = 0
    table_dict = {g: list() for g in keyword}
    while dex < len(fractionated):
        for h in keyword:
            try:
                table_dict[h].append(fractionated[dex])
                dex += 1
            except IndexError:
                break
    return ''.join(''.join(v) for k, v in sorted(table_dict.items()))


def decode(message, secret_alphabet, keyword):
    cipher_dict = create_table(secret_alphabet, to_encode=False)
    keyword = clean_keyword(keyword)
    msg_len = len(message)
    key_len = len(keyword)
    if msg_len % key_len == 0:
        full = msg_len // key_len
        d = {a: full for a in keyword}

    else:
        for a in range(1, msg_len):
            if a * key_len > msg_len:
                full = a                         # maximum for full columns
                diff = full * key_len - msg_len  # num of columns missing
                break
        d = dict()
        for i, char in enumerate(keyword):
            if i < key_len - diff:
                d[char] = full
            else:
                d[char] = full - 1
    dex = 0
    column = dict()
    for letter, value in sorted(d.items()):
        if value == full:
            column[letter] = list(message[dex:dex+full])
            dex += full
        else:
            column[letter] = list(message[dex:dex+(full-1)] + ' ')
            dex += full - 1

    msg = ''.join(''.join(g) for g in zip(*[column[char]
                                            for char in keyword])).strip()
    return ''.join(cipher_dict[msg[h:h+2]] for h in range(0, len(msg), 2))


# print(encode('I am going.', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g', 'cipher')) == 'FXGAFVXXAXDDDXGA'
# print(decode('FXGAFVXXAXDDDXGA', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g', 'cipher')) == 'iamgoing'

if __name__ == '__main__':
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
    assert decode("FXGAFVXXAXDDDXGA",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'iamgoing', "decode I am going"
    assert encode("attack at 12:00 am",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
    assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'attackat1200am', "decode attack"
    assert encode("ditiszeergeheim",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
    assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
    assert encode("I am going",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
    assert decode("DXGAXAAXXVDDFGFX",
                  "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'iamgoing', "decode weasel == weasl"
