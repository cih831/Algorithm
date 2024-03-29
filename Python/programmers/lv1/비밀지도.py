def solution(n, arr1, arr2):
    return list(('0' * n + bin(arr1[i]|arr2[i])[2:])[-n:].replace('1', '#').replace('0', ' ') for i in range(n))

print(solution(
    6,
    [46, 33, 33, 22, 31, 50],
    [27, 56, 19, 14, 14, 10]
    ))

# ["######","###  #","##  ##","#### ","#####","### # "]
# ["######","###  #","##  ##"," #### "," #####","### # "]