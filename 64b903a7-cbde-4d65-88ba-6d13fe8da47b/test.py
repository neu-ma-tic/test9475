'''import numpy as np

a = set()
arr = np.array([
      [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
      [0, 0, 1, 0, 0, 0, 1, 3, 0, 1],
      [0, 1, 1, 0, 0, 4, 3, 3, 3, 1],
      [0, 1, 0, 0, 4, 0, 1, 5, 3, 1],
      [1, 1, 0, 1, 1, 4, 1, 0, 1, 1],
      [1, 0, 0, 0, 4, 0, 0, 4, 0, 1],
      [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
      [1, 1, 1, 1, 1, 1, 1, 2, 0, 1],
      [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
    ], dtype='i')

rows, cols = arr.shape
for i in range(rows):
  for j in range(cols):
    if arr[i, j] in {3, 5}:
      a.add((i, j))
    if arr[i, j] == 2:
      print((i, j))

print(a)'''
