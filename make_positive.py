def make_positive(a):
  for i in range(len(a)):
    if a[i] < 0:
      a[i] = -a[i]
  return a

print(make_positive( [-3, 1, -2, 5, -3]))