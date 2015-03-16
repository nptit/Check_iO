def checkio(time_string):
    h, m, s = (tuple(a.zfill(2)) for a in time_string.split(':'))
    print(h, m, s)
    # '{:0>{length}b}'.format(3, length=4)


checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-"
# checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--."
# checkio("00:1:02") == ".. .... : ... ...- : ... ..-."
# checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-"

# if __name__ == '__main__':
#     assert checkio("10:37:49") == ".- .... : .-- .--- : -.. -..-", "First Test"
#     assert checkio("21:34:56") == "-. ...- : .-- .-.. : -.- .--.", "Second Test"
#     assert checkio("00:1:02") == ".. .... : ... ...- : ... ..-.", "Third Test"
#     assert checkio("23:59:59") == "-. ..-- : -.- -..- : -.- -..-", "Fourth Test"
