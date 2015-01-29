def count_inversion(sequence):
    """ Count inversions in a sequence of numbers """
    return sum(sum(1 for b in sequence[i+1:] if a > b)
               for i, a in enumerate(sequence))

if __name__ == '__main__':
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
