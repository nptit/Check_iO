def translate(phrase):
    dex = 0
    plain = list()
    vowels = 'aeiouy'
    while dex < len(phrase):
        current = phrase[dex]
        if current in vowels:    # vowels
            dex += 3
        elif current.isalpha():  # consonants
            dex += 2
        else:                    # all other characters (spaces, punctuation)
            dex += 1
        plain.append(current)
    return ''.join(plain)

if __name__ == '__main__':
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"
