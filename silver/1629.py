def d(a, b, c):
  if b == 1:
    return a % c
  elif b % 2 == 0:
    return (d(a, b//2, c) ** 2) % c
  else:
    return ((d(a, b//2, c) ** 2) * a) % c

A, B, C = map(int, input().split())

print(d(A, B, C))