N = int(input())
text = input()
H = 0

for i in range(len(text)):
    H += (ord(text[i]) - ord('a') + 1) * (31**i)

print(H % 1234567891)

