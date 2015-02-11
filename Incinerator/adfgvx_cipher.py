def encode(message, secret_alphabet, keyword):
    msg = ''.join(a.lower() for a in message if a.isalnum())
    adfgvx = {b: c for b, c in zip(range(6), 'ADFGVX')}
    dex = 0
    table = dict()
    for d in range(6):
        for e in range(6):
            table[secret_alphabet[dex]] = ''.join((adfgvx[d], adfgvx[e]))
            dex += 1

    new_table = ''.join(table[char] for char in msg)
    #print(new_table)
    dex = 0
    table_dict = {g: list() for g in keyword}
    while dex < len(new_table):
        for h in keyword:
            try:
                table_dict[h].append(new_table[dex])
                dex += 1
            except IndexError:
                pass
    return ''.join(''.join(table_dict[i]) for i in sorted(table_dict.keys()))


def decode(message, secret_alphabet, keyword):
    return message


print(encode('I am going.', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g', 'cipher')) == 'FXGAFVXXAXDDDXGA'
print(decode('FXGAFVXXAXDDDXGA', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g', 'cipher')) == 'iamgoing'

# if __name__ == '__main__':
#     assert encode("I am going",
#                   "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
#                   "cipher") == 'FXGAFVXXAXDDDXGA', "encode I am going"
#     assert decode("FXGAFVXXAXDDDXGA",
#                   "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
#                   "cipher") == 'iamgoing', "decode I am going"
#     assert encode("attack at 12:00 am",
#                   "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
#                   "privacy") == 'DGDDDAGDDGAFADDFDADVDVFAADVX', "encode attack"
#     assert decode("DGDDDAGDDGAFADDFDADVDVFAADVX",
#                   "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
#                   "privacy") == 'attackat1200am', "decode attack"
#     assert encode("ditiszeergeheim",
#                   "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
#                   "piloten") == 'DFGGXXAAXGAFXGAFXXXGFFXFADDXGA', "encode ditiszeergeheim"
#     assert decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA",
#                   "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz",
#                   "piloten") == 'ditiszeergeheim', "decode ditiszeergeheim"
#     assert encode("I am going",
#                   "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
#                   "weasel") == 'DXGAXAAXXVDDFGFX', "encode weasel == weasl"
#     assert decode("DXGAXAAXXVDDFGFX",
#                   "dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g",
#                   "weasel") == 'iamgoing', "decode weasel == weasl"
