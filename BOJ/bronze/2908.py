a, b = input().split()

x = ''
y = ''

for i in range(1, 4):
    x += a[-i]
    y += b[-i]

x, y = int(x), int(y)

if x > y:
    print(x)
else:
    print(y)