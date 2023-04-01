def recur():
    global nc
    i = 0
    while '+' in nc:
        if nc[i+1] == '+':
            nc = nc[:i] + [nc[i]+nc[i+2]] + nc[i+3:]
        else:
            i += 2
    while len(nc) != 1:
        nc = [nc[0] - nc[2]] + nc[3:]

F = list(input())
nc = ['']
for item in F:
    if not item in '+-':
        nc[-1] = nc[-1] + item
    else:
        nc[-1] = int(nc[-1])
        nc.append(item)
        nc.append('')
nc[-1] = int(nc[-1])
recur()
print(nc[0])
