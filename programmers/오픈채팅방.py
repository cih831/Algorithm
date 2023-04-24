def solution(record):
    answer = []
    d = {}

    for rec in record:
        tmp = rec.split()
        if not tmp[0] == 'Leave': # 닉네임을 UID에 반영
            d[tmp[1]] = tmp[2]
        if not tmp[0] == 'Change': # 닉변이 아니면 입출입 직어주기
            answer.append((tmp[0], tmp[1]))

    for i in range(len(answer)): # 문자열로 변환
        answer[i] = f'{d[answer[i][1]]}님이 ' + ('들어왔습니다.' if answer[i][0] == 'Enter' else '나갔습니다.')

    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))