def checkio(opacity):
    fibonacci = [1, 1]
    while True:                          # create list of fibonacci numbers
        current = sum(fibonacci[-2:])
        fibonacci.append(current)
        if current > 10000:
            break

    ghost_age = 0
    ghost_opacity = 10000
    while not ghost_opacity == opacity:  # calculate ghost age
        ghost_age += 1
        if ghost_age not in fibonacci:
            ghost_opacity += 1           # if age not fibonacci, add opacity
        else:
            ghost_opacity -= ghost_age   # if age is fibonacci, reduce opacity
    return ghost_age

if __name__ == '__main__':
    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
