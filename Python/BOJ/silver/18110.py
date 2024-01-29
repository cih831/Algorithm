import sys

input = sys.stdin.readline


def _round(num):
    return int(num) + 1 if num - int(num) >= 0.5 else int(num)


n = int(input())
arr = sorted([int(input()) for _ in range(n)])[
    _round(n * 0.15) : -_round(n * 0.15) if _round(n * 0.15) else None
]
print(_round(sum(arr) / len(arr)) if arr else 0)
