def solution(s):
    answer = []
    lst = [tuple(map(int, item.split(","))) for item in tuple(map(str, s[2:-2].split("},{")))]
    
    # 집합의 길이가 짧을수록 작은 숫자이기 때문에, 비트마스킹으로 표현 이후 정렬
    sorted_bin = [0]
    for tp in lst:
        tmp = 0
        for num in tp:
            tmp |= 1 << num
        sorted_bin.append(tmp)
    sorted_bin.sort()
    
    # 이전 집합과 비교하여 새로 추가된 원소를 answer에 append
    for i in range(len(sorted_bin) - 1):
        answer.append(bin(sorted_bin[i] ^ sorted_bin[i + 1])[2:].count('0'))
    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
