def checkio(data):
    roman_numerals = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
                      100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
                      9: 'IX', 4: 'IV', 5: 'V', 1: 'I'}
    converted = list()
    for numeral in sorted(roman_numerals, reverse=True):
        numeral_multiplier, remainder = divmod(data, numeral)
        if not numeral_multiplier == 0:
            converted.append(roman_numerals[numeral] * numeral_multiplier)
            data = remainder
    return ''.join(converted)

if __name__ == '__main__':
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
