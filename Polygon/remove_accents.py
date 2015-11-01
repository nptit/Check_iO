from unicodedata import category, normalize


def checkio(txt):
    return ''.join(a for a in normalize('NFD', txt) if category(a) != 'Mn')

if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
