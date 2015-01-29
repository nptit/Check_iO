from string import ascii_lowercase


def check_pangram(text):
    return set(a.lower() for a in text if a.isalpha()) ==\
           set(b for b in ascii_lowercase)

if __name__ == '__main__':
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
