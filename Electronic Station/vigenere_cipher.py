from string import ascii_uppercase


def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    a_z = ascii_uppercase
    # key = [(26 - a_z.index(b) + a_z.index(a)) % 26
    #        for a, b in zip(old_decrypted, old_encrypted)]
    # key_len = len(key)
    # return ''.join(a_z[(key[c % key_len] + a_z.index(char)) % 26]
    #                for c, char in enumerate(new_encrypted))
    key = list()
    for a, b in zip(old_decrypted, old_encrypted):
        key.append(a_z[(26 - a_z.index(b) + a_z.index(a)) % 26])

    print('%', ''.join(key))
    key = [a_z.index(c) for c in non_repeating_key(''.join(key))]
    print(''.join(a_z[d] for d in key))
    key_len = len(key)
    new_decrypted = list()
    for c, char in enumerate(new_encrypted):
        new_decrypted.append(a_z[(key[c % key_len] + a_z.index(char)) % 26])
    return ''.join(new_decrypted)


def non_repeating_key(txt):
    unique = set(txt)
    if len(unique) == 1:  # if the key is a single character repeated
        return ''.join(unique)

    chunks = set()
    length = len(txt)
    for a in range(2, length+1):  # minimum chunk size of 2
        chunk = txt[0:a]
        chunks.add((txt.count(chunk), len(chunk), chunk))
    [print(b) for b in sorted(chunks)]

    # maybe some sort of calculation between length of chunk,
    # times size of chunk, compared to length of txt??
    key = None
    for b in sorted(chunks, reverse=True):
        if key is None or len(b[2]) > len(key):
            key = b[2]
        else:
            break
    return key


print(non_repeating_key('UGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGSXMUGS'))

# decode_vigenere(u"ITSNOTPININGITSPASSEDONTHISPARROTISNOMOREITHASCEASEDTOBEITSEXPIREDANDGONETOMEETITSMAKERTHISISALATEPARROTITSASTIFFBEREFTOFLIFEITRESTSINPEACEIFYOUHADNTNAILEDITTOTHEPERCHITWOULDBEPUSHINGUPTHEDAISIESITSRUNGDOWNTHECURTAINANDJOINEDTHECHOIRINVISIBLETHISISANEXPARROT", u"ONAQCZJQQWTAQWGVUAVSJIVWVOMXDFXIBLGTIURFKCBKOYWMDGKXBRPKCBVSDJQUSJUVGUUHMWCSYMWWZMUDYKLBKWYCADZGNMSOXLWWWZMIVHOZNESXYNWCLFQISONZHGZMQQDKUKHWLSWXVGXVWBGCTHRONBRHNYXHFIBQWKUOTGPKJCVVOHOXDZBMGOOMQHGONAUITALRKTNPHQALBDWTUVGXUCVHRZBMFVUCZLBBCALPRYBKWYCADBKRXDFXIB", u"GFTUWMBBDZRLQJVZVCWOVUZWTXIUESZNMUGGHQWOZCWQOTXUHROWQQSGHLHRAWIWWUHIQROLZLUGNQRBGHLSIHFQFVKUTWVGHLUCGXADBJUNUSYBEDHKLABGZYUDBJVIWVYUVGDAVTLQULLHFCBIWVGPMWVKLWPOTMMYSXXWQSLIZXG")

# print(non_repeating_key('YTWYQSMYTWYQSMYT'))

# print(decode_vigenere(u"DONTWORRYBEHAPPY", u"FVRVGWFTFFGRIDRF", u"DLLCZXMFVRVGWFTF"))

# print(non_repeating_key('WFWJCZMXCWFWJCZMXCWFWJCZMXCWFWJCZMXCWFWJCZMXCWFWJCZMXCWFWJCZMXCWFWJCZMXCWFWJCZMXCWFWJCZMXCWFWJCZMXCWFWJCZMXCWFWJCZMXCWFWJCZMXCWFWJCZMXC'))

# print(decode_vigenere(u"IMALUMBERJACKANDIMOKISLEEPALLNIGHTANDIWORKALLDAYICUTDOWNTREESISKIPANDJUMPILIKETOPRESSWILDFLOWERSIPUTONWOMENSCLOTHINGANDHANGAROUNDINBARS", u"MHECSNPHPNVGBYORLKSFMJJFSSYPGRZEIHDLHDAFPLOOJHVCZAVHGMAIXICFGLQODTRLEXXKTDPZIFHRNVZWJUJZGDPJAVPTWSSXJRNMNSQQGGSKFJBJYRYLRLHOUMYIHZLCOUQ", u"EIHEMXTRPWJQVRIWQEGJQGJFHHJCYMWDFFHLX"))
# print(decode_vigenere(u"ANDNOWFORSOMETHINGCOMPLETELYDIFFERENT", u"PLWUCJUMKZCZTRAPBTRMFWZRICEFRVUDXYSAI", u"XKTSIZQCKQOPZYGKWZDIBZZRTNTSZAXEAAOASGPVFXPJEKOLXANARBLLMYSRHGLRWCPLWQIZEGEPYRIMIYSFHUBSRSAMPLFFXNNACALMFLBFRJHAVVCETURUPLZHFBJLWPBOPPL"))

# print(non_repeating_key('LCHTMNLCHTMNLCHTMNLCHTMNLCHTMNLCHTMNL'))

# print('*' * 30)
# print(non_repeating_key('LLLLLLLLLLLLLLLLL'))

# print(decode_vigenere('DONTWORRYBEHAPPY',
#                        'FVRVGWFTFFGRIDRF',
#                        'DLLCZXMFVRVGWFTF'))  # == "BEHAPPYDONTWORRY"
# print(decode_vigenere('HELLO', 'OIWWC', 'ICP'))  # == "BYE"
# print(decode_vigenere('LOREMIPSUM',
#                        'OCCSDQJEXA',
#                        'OCCSDQJEXA'))  # == "LOREMIPSUM", "DOLORIUM"

# # if __name__ == '__main__':
# #     assert decode_vigenere('DONTWORRYBEHAPPY',
# #                            'FVRVGWFTFFGRIDRF',
# #                            'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY", "CHECKIO"
# #     assert decode_vigenere('HELLO', 'OIWWC', 'ICP') == "BYE", "HELLO"
# #     assert decode_vigenere('LOREMIPSUM',
# #                            'OCCSDQJEXA',
# #                            'OCCSDQJEXA') == "LOREMIPSUM", "DOLORIUM"
