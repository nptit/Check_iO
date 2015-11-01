def find_word(message):
    word_percentages = dict()
    words = ''.join(a.lower() for a in message
                    if a.isspace() or a.isalpha()).split()
    for dex, word in enumerate(words):
        for dex2, word2 in enumerate(words):
            if dex == dex2 and word == word2:
                continue
            total = 0
            if word[0] == word2[0]:    # first letters match
                total += 10
            if word[-1] == word2[-1]:  # last letters match
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
            if (word2, dex2) not in word_percentages:
                word_percentages[(word2, dex2)] = list()
            word_percentages[(word2, dex2)].append(round(total, 3))

    scores = dict()
    for word_pair, percentages in word_percentages.items():
        word, index = word_pair
        average = round(sum(percentages) / len(percentages), 3)
        if average in scores:  # choose highest index on conflicts
            s_word, s_index = scores[average]
            if index > s_index:
                scores[average] = word_pair
        else:                  # unique/first average key in scores
            scores[average] = word_pair
    return scores[max(scores)][0]

if __name__ == '__main__':
    assert find_word('Friend Fred and friend Ted.') == "friend"
    assert find_word("Speak friend and enter.") == "friend"
    assert find_word("Beard and Bread") == "bread"
    assert find_word(
        "The Doors of Durin, Lord of Moria. Speak friend and enter. "
        "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") \
        == "according"
    assert find_word("One, two, two, three, three, three.") == "three"
