from itertools import zip_longest


def decode_amsco(message, key):
    key_str = str(key)
    key_len = len(key_str)
    column_indices = {int(a): list() for a in key_str}
    msg_len = len(message)
    dex = 0       # index of current position in message
    cnt = 1       # either 1 or 2 for chunk size out of message
    key_dex = 0
    first = None  # first in row, makes columns alternate 1 or 2 length
    while dex < msg_len:
        mod = key_dex % key_len
        if mod == 0 and first is None:        # very first
            first = cnt
        elif mod == 0 and first is not None:  # first in following rows
            cnt = 2 if first == 1 else 1
            first = cnt

        if dex + cnt > msg_len:               # if +2 is too much
            cnt = 1

        column_indices[int(key_str[mod])].append(cnt)
        dex += cnt
        cnt = 2 if cnt == 1 else 1
        key_dex += 1

    msg_dex = 0
    matrix = {b: list() for b in key_str}
    for k, v in column_indices.items():       # go through indices, get slices
        current_key = str(k)
        matrix[current_key] = list()
        for index in v:                       # append slices from message
            matrix[current_key].append(message[msg_dex:msg_dex+index])
            msg_dex += index

    return ''.join(''.join(line) for line in zip_longest(
        *(matrix[a] for a in key_str), fillvalue=''))

if __name__ == '__main__':
    assert decode_amsco("oruoreemdstmioitlpslam", 4123) == "loremipsumdolorsitamet", "Lorem Ipsum"
    assert decode_amsco('kicheco', 23415) == "checkio", "Checkio"
    assert decode_amsco('hrewhoorrowyilmmmoaouletow', 123) == "howareyouwillhometommorrow", "How are you"
