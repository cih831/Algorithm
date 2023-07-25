def solution(s):
    cnt = 0
    for item in s:
        cnt = cnt + 1 if item == "(" else cnt - 1 if cnt else int(1e9)
    return cnt == 0