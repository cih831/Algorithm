def fac(x):
    res = 1
    for num in range(1, x + 1):
        res *= num
    return res

n, m = map(int, input().split())
print(fac(n) // (fac(n - m) * fac(m)))