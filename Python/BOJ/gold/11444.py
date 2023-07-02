import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
fibonacci = {0: 0, 1: 1, 2: 1}


def fibo(n):
    if not fibonacci.get(n):
        if n % 2 == 1:
            fibonacci[n] = (fibo((n+1)//2)**2 + fibo((n+1)//2-1)**2) % 1000000007
        else:
            fibonacci[n] = (fibo(n+1) - fibo(n-1)) % 1000000007

    return fibonacci[n]

N = int(input())
print(fibo(N))