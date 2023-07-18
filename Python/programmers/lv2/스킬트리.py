"""
정규표현식
"[CBD]" => 대괄호 안에 포함된 문자들 중 하나와 매치
"^ABC" => ABC로 시작하는 문자열과 매치

re.findall => 모든 매치를 찾아 리스트로 반환
re.search => 문자열에서 검색하여 처음으로 매치되는 문자열을 찾음
"""

def solution(skill, skill_trees):
    from re import search, findall
    answer = 0
    for skill_tree in skill_trees:
        if search(f'^{"".join(findall(f"[{skill}]", skill_tree))}', skill):
            answer += 1
    return answer

print(solution(
    "CBD",
    ["BACDE", "CBADF", "AECB", "BDA"]
))