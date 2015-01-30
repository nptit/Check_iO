def checkio(n):
    words = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
             11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
             15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
             19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
             50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
             90: 'ninety', 100: 'hundred', 1000: 'thousand'}
    k = sorted(words.keys(), reverse=True)
    if n in k:
        if n == 100 or n == 1000:
            return 'one ' + words[n]
        return words[n]
    else:
        lst = list()
        for x in k:
            if x <= n:
                cnt = n // x  # how many?
                n -= x * cnt  # subtract each from original 'n'
                if x == 100 or x == 1000:  # add 'how many' to 100's or 1000's
                    lst.append(words[cnt])
                lst.append(words[x])
        return ' '.join(lst)

if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
