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


def decode(message, secret_alphabet, keyword):
    cipher_dict = create_table(secret_alphabet, to_encode=False)
    keyword = clean_keyword(keyword)
    msg_len = len(message)
    keyword_len = len(keyword)
    if msg_len % keyword_len == 0:  # keyword_len divides evenly into msg_len
        full = msg_len // keyword_len  # all columns are same length
        keyword_char_values = {a: full for a in keyword}
    else:
        for f in range(1, msg_len):
            if f * keyword_len > msg_len:
                full = f                             # maximum for full columns
                diff = full * keyword_len - msg_len  # num of columns missing 1
                break
        keyword_char_values = dict()
        for g, char in enumerate(keyword):
            if g < keyword_len - diff:
                keyword_char_values[char] = full
            else:
                keyword_char_values[char] = full - 1
    dex = 0
    column = dict()
    for letter, value in sorted(keyword_char_values.items()):
        if value == full:
            column[letter] = list(message[dex:dex+full])
            dex += full
        else:
            column[letter] = list(message[dex:dex+(full-1)] + ' ')
            dex += full - 1
    msg = ''.join(''.join(h) for h in zip(*[column[char]
                                            for char in keyword])).strip()
    return ''.join(cipher_dict[msg[i:i+2]] for i in range(0, len(msg), 2))


def encode(message, secret_alphabet, keyword):
    msg = ''.join(j.lower() for j in message if j.isalnum())
    cipher_dict = create_table(secret_alphabet)
    fractionated = ''.join(cipher_dict[char] for char in msg)
    keyword = clean_keyword(keyword)
    dex = 0
    table_dict = {k: list() for k in keyword}
    while dex < len(fractionated):
        for l in keyword:
            try:
                table_dict[l].append(fractionated[dex])
                dex += 1
            except IndexError:
                break
    return ''.join(''.join(m) for _, m in sorted(table_dict.items()))

if __name__ == '__main__':
    assert encode("I am going", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'FXGAFVXXAXDDDXGA'
    assert decode("FXGAFVXXAXDDDXGA", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "cipher") == 'iamgoing'
    assert encode("attack at 12:00 am", "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX'
    assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz", "privacy") \
        == 'attackat1200am'
    assert encode("ditiszeergeheim", "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
                  "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA'
    assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
                  "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz", "piloten") \
        == 'ditiszeergeheim'
    assert encode("I am going", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'DXGAXAAXXVDDFGFX'
    assert decode("DXGAXAAXXVDDFGFX", "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
                  "weasel") == 'iamgoing'
