N, M = map(int, input().split())
T = set(list(map(int, input().split()))[1:])
arr = [list(map(int, input().split()))[1:] for _ in range(M)]
cnt = M
cnt2 = 0

while cnt != cnt2:
    cnt2 = cnt
    delete = []
    for party in range(len(arr)):
        for people in arr[party]:
            if people in T:
                T = T | set(arr[party])
                cnt -= 1
                delete.append(party)
                break
    for party in reversed(delete):
        arr.pop(party)

print(cnt)