from hashlib import md5, sha1, sha224, sha256, sha384, sha512


def checkio(hashed_string, algorithm):
    if algorithm == 'md5':
        return md5(hashed_string.encode()).hexdigest()
    elif algorithm == 'sha1':
        return sha1(hashed_string.encode()).hexdigest()
    elif algorithm == 'sha224':
        return sha224(hashed_string.encode()).hexdigest()
    elif algorithm == 'sha256':
        return sha256(hashed_string.encode()).hexdigest()
    elif algorithm == 'sha384':
        return sha384(hashed_string.encode()).hexdigest()
    elif algorithm == 'sha512':
        return sha512(hashed_string.encode()).hexdigest()

if __name__ == '__main__':
    assert checkio('welcome', 'md5') == '40be4e59b9a2a2b5dffb918c0e86b3d7'
    assert checkio('happy spam', 'sha224') \
        == '6e9dc3e01d57f1598c2b40ce59fc3527e698c77b15d0840ae96a8b5e'
