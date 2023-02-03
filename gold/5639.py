import sys
sys.setrecursionlimit(1000000)

def recur(root, right):
    if right - 1 == root:
        print(arr[root])
        return
    for i in range(root, right):
        if arr[i] > arr[root]:
            recur(root + 1, i)
            recur(i, right)
            print(arr[root])
            break
    else:
        if root < right:
            recur(root + 1, right)
            print(arr[root])
            

arr = []
while 1:
    try:
        arr.append(int(input()))
    except:
        break

recur(0, len(arr))