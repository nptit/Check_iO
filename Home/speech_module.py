WORDS = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
    19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
    50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
    90: 'ninety', 100: 'hundred', 1000: 'thousand'}


def checkio(n):
    result = []
    for k in sorted(WORDS.keys(), reverse=True):
        if k <= n:
            q, r = divmod(n, k)
            n = r
            result.append(WORDS[q] + ' ' + WORDS[k] if k >= 100 else WORDS[k])
    return ' '.join(result)

if __name__ == '__main__':
    assert checkio(4) == 'four'
    assert checkio(133) == 'one hundred thirty three'
    assert checkio(12) == 'twelve'
    assert checkio(101) == 'one hundred one'
    assert checkio(212) == 'two hundred twelve'
    assert checkio(40) == 'forty'
    assert not checkio(212).endswith(' ')
