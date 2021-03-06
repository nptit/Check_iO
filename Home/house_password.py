def checkio(pw):
    if len(pw) >= 10:
        upper = False
        lower = False
        digit = False
        for char in pw:
            if char.isupper():
                upper = True
            elif char.islower():
                lower = True
            elif char.isdigit():
                digit = True
        if upper and lower and digit:
            return True
    return False

if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
