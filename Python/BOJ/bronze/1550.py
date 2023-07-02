N = input()
alpha = 'ABCDEF'
num = 0
for i in range(len(N)):
    for j in range(len(alpha)):
        if N[i] == alpha[j]:
            num += (10 + j) * (16**(len(N)-i-1))
            break
    else:
        num += int(N[i])*(16**(len(N)-i-1))

print(num)