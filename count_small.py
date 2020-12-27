def count_small(a):
  count = 0
  for i in range(len(a)):
    if a[i] in range(0, 100):
      count = count + 1
  return count


print(count_small([-1, 10, 1, 100, 200, 20, 10, 0]))