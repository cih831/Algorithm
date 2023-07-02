def solution(want, number, discount):
    from copy import deepcopy
    answer = 0
    lst = []
    for i in range(len(want)):
        lst.extend([want[i]] * number[i])

    for i in range(len(discount) - sum(number) + 1):
        tmp = deepcopy(lst)
        if discount[i] in tmp:
            for j in range(sum(number)):
                if discount[i + j] in tmp:
                    tmp.remove(discount[i + j])
                else:
                    break
            else:
                answer += 1
    return answer

print(solution(
    ["banana", "apple", "rice", "pork", "pot"],
    [3, 2, 2, 2, 1],
    ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
))