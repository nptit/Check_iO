def checkio(w, w2):
    return ','.join(sorted(set(w.split(',')).intersection(set(w2.split(',')))))

if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") \
        == "one,three,two", "1 2 3"
