def find_word(message):
    words = ''.join(a.lower() for a in message
                    if a.isspace() or a.isalpha()).split()
    print(words)
    unique_words = set(words)
    unique_len = len(unique_words)

    d = {word: list() for word in words}  # percentages
    for dex, word in enumerate(words):
        # still have duplicates in dictionary for non-unique words!!
        for dex2, word2 in enumerate(words):
            if dex == dex2 or word == word2:
                continue
            total = 0
            if word[0] == word2[0]:
                total += 10
            if word[-1] == word2[-1]:
                total += 10

            word_len = len(word)
            word2_len = len(word2)
            if word_len <= word2_len:
                total += (word_len / word2_len) * 30
            else:
                total += (word2_len / word_len) * 30

            word_set = set(word)
            word2_set = set(word2)
            diff = len(word_set.union(word2_set))
            same = len(word_set.intersection(word2_set))
            total += (same / diff) * 50

            d[word2].append(round(total, 3))
    print(d)
    print()


find_word('Friend Fred and friend Ted.') == "friend"
find_word("Speak friend and enter.") == "friend"


# if __name__ == '__main__':
#     assert find_word("Speak friend and enter.") == "friend", "Friend"
#     assert find_word("Beard and Bread") == "bread", "Bread is Beard"
#     assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
#                      "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
#     assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
#                      " According to a researcher at Cambridge University.") == "according", "Research"
#     assert find_word("One, two, two, three, three, three.") == "three", "Repeating"
