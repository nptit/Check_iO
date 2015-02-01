from collections import Counter


def verify_anagrams(x, y):
    return True if Counter(a.lower() for a in x if a.isalpha()) == \
        Counter(b.lower() for b in y if b.isalpha()) else False

if __name__ == '__main__':
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
