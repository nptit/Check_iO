from string import ascii_uppercase


def decode_vigenere(old_decrypted, old_encrypted, new_encrypted):
    a_z = ascii_uppercase
    key = ''.join(a_z[(26 - a_z.index(b) + a_z.index(a)) % 26]
                  for a, b in zip(old_decrypted, old_encrypted))
    clean_key = [a_z.index(c) for c in clean_up_key(key)]
    key_len = len(clean_key)
    return ''.join(a_z[(clean_key[c % key_len] + a_z.index(char)) % 26]
                   for c, char in enumerate(new_encrypted))


def clean_up_key(txt):
    if len(set(txt)) == 1:        # if key is a single character repeated
        return txt[0]

    length = len(txt)
    longest = None
    for a in range(2, length+1):  # minimum chunk size of 2
        chunk = txt[0:a]
        chunk_cnt = 0
        for b in range(0, length, a):
            end = a + b
            if a + b > length and chunk == txt[b:length]:
                end = length
            if chunk == txt[b:end] or chunk.startswith(txt[b:end]):
                chunk_cnt += 1
        current = (chunk_cnt, len(chunk), chunk)
        if longest is None or current > longest:
            longest = current
    return longest[2]             # return string only

if __name__ == '__main__':
    assert decode_vigenere('DONTWORRYBEHAPPY',
                           'FVRVGWFTFFGRIDRF',
                           'DLLCZXMFVRVGWFTF') == "BEHAPPYDONTWORRY", "CHECKIO"
    assert decode_vigenere('HELLO', 'OIWWC', 'ICP') == "BYE", "HELLO"
    assert decode_vigenere('LOREMIPSUM',
                           'OCCSDQJEXA',
                           'OCCSDQJEXA') == "LOREMIPSUM", "DOLORIUM"
