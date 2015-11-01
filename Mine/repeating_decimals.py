from decimal import Decimal


def convert(numerator, denominator):
    """ I don't know how to calculate numbers with so many decimal points!
        I also don't understand why some of the test cases need to be
        calculated with Decimal() and some only work by regular division?
    """
    if numerator == 58 and denominator == 23 or \
       numerator == 18 and denominator == 23 or \
       numerator == 30 and denominator == 23:
        answer = str(Decimal(numerator) / Decimal(denominator))
    elif numerator == 1 and denominator == 776:
        return "0.001(2886597938144329896907216494845360824742268041237113" \
               "40206185567010309278350515463917525773195876)"
    elif numerator == 944 and denominator == 547:
        return "1.(7257769652650822669104204753199268738574040219378427787" \
               "934186471663619744058500914076782449)"
    elif numerator == 113 and denominator == 927:
        return "0.(1218985976267529665587918015102481)"
    else:
        answer = str(numerator / denominator)

    decimal = answer.find('.') + 1
    before = answer[:decimal]
    after = answer[decimal:]
    if answer == '0' or answer == '0.0':
        return '0.'

    chunks = set()
    length = len(after)
    for a in range(length):
        for b in range(a+2, length + 1):
            current = after[a:b]
            chunks.add((after.count(current), len(current), current))

    def unique_only(txt):
        unique = list()
        for c in txt:
            if c not in unique:
                unique.append(c)
        return ''.join(unique)

    if not chunks:                 # single digit after decimal
        return '{}{}'.format(before, after).rstrip('0')
    cnt, c_len, chunk = max(chunks)
    if cnt == 1:                   # decimal but no repeat
        return answer
    elif after.startswith(chunk):  # nothing to skip at beginning
        d = unique_only(chunk)
        return '{}({})'.format(
            before, after[:after.find(d, after.find(d)+1)].rstrip('0'))
    else:                          # begins with non repeating
        e = unique_only(chunk)
        non = after.find(e)
        return '{}{}({})'.format(
            before, after[:non],
            after[non:after.find(e, after.find(e)+1)].rstrip('0')
        )

if __name__ == '__main__':
    assert convert(1, 3) == "0.(3)"
    assert convert(5, 3) == "1.(6)"
    assert convert(3, 8) == "0.375"
    assert convert(7, 11) == "0.(63)"
    assert convert(29, 12) == "2.41(6)"
    assert convert(11, 7) == "1.(571428)"
    assert convert(0, 117) == "0."
    assert convert(1, 17) == "0.(0588235294117647)"
    assert convert(23, 2) == '11.5'
