from collections import Counter


def verify_anagrams(x, y):
    return True if Counter(a.lower() for a in x if a.isalpha()) == \
        Counter(b.lower() for b in y if b.isalpha()) else False

if __name__ == '__main__':
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") is True
    assert verify_anagrams("Hello", "Ole Oh") is False
    assert verify_anagrams("Kyoto", "Tokyo") is True
