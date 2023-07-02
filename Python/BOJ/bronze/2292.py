# 1 - 7 - 19 -  37 - 61 ...
# i * 6 + 1

N = int(input())
B = [1]
i = 1

while B[-1] < N:
    B += [B[-1] + i * 6]
    i += 1

i = 0

while B[i] < N:
    i += 1

print(i+1)