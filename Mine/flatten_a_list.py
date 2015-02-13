def flat_list(a):
  for i,x in enumerate(a):
    try:
      while type(a[i])==list:a[i:i+1]=a[i]
    except IndexError:pass
  return a

assert flat_list([1, 2, 3]) == [1, 2, 3]
assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4]
assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1]
assert flat_list([[[[[[[[[]]]]]]]]]) == []
assert flat_list([[[2]],[4,[5,6,[6],6,6,6],7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7]
