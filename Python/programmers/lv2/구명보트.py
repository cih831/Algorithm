def solution(people, limit):
    answer = 0
    people.sort()
    s, e = 0, len(people) - 1
    while s < e:
        if people[s] + people[e] <= limit:
            if e - s == 2:
                answer += 1
            s += 1
        elif e - s == 1:
            answer += 1
        e -= 1
        answer += 1
    return answer

print(solution([70, 50, 80, 50], 100))