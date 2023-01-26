num = list(map(int, input().split()))
num.sort()
a, b = num[0], num[1]


while b % a != 0:
    a, b = b % a, a

print(a)
b = num[0] * num[1] // a
print(b)