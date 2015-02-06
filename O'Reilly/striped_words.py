def checkio(text):
    vowels = set('AEIOUY')
    consonants = set('BCDFGHJKLMNPQRSTVWXZ')
    words = ''.join(a.upper() if a.isalnum() else ' ' for a in text).split()
    total_striped = 0

    for word in words:
        striped = False
        if word.isalpha() and len(word) > 1:  # skip if too short or has digits
            striped = True
            vow, con = 0, 0
            for char in word:
                if char in vowels:
                    vow += 1
                    con = 0
                elif char in consonants:
                    con += 1
                    vow = 0
                if vow == 2 or con == 2:
                    striped = False
                    break
        if striped:
            total_striped += 1
    return total_striped

if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
