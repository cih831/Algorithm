import sys

input = sys.stdin.readline

def pre_order(r):
    if r == '.':
        return
    print(r, end='')
    pre_order(d[r][0])
    pre_order(d[r][1])

def in_order(r):
    if r == '.':
        return
    in_order(d[r][0])
    print(r, end='')
    in_order(d[r][1])

def post_order(r):
    if r == '.':
        return
    post_order(d[r][0])
    post_order(d[r][1])
    print(r, end='')

N = int(input())

d = {}
for _ in range(N):
    Root, Left, Right = input().split()
    d[Root] = [Left, Right]

pre_order('A')
print()
in_order('A')
print()
post_order('A')