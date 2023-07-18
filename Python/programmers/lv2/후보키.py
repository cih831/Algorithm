from itertools import combinations

def solution(relation):
    answer_lst = []
    n = len(relation)
    m = len(relation[0])
    combi = []
    for i in range(1, m + 1):
        combi.extend(combinations(range(m), i))

    for i in combi:
        tmp = set(tuple(item[key] for key in i) for item in relation)

        if len(tmp) != n:
            continue

        for item in answer_lst:
            if item.issubset(set(i)):
                break
        else:
            answer_lst.append(set(i))

    answer = len(answer_lst)
    return answer

ip = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
      ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
# ip = [["100","100","ryan","music","2"], ["200","200","apeach","math","2"], ["300","300","tube","computer","3"], ["400","400","con","computer","4"], ["500","500","muzi","music","3"], ["600","600","apeach","music","2"]]
print(solution(ip))