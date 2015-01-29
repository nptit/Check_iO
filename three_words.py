def checkio(words):
    words = words.split()
    for i in range(len(words) - 2):
        if all(a.isalpha() for a in words[i:i+3]):
            return True
    return False 

if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
