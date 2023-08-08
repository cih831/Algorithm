def solution(dartResult):
    answer = 0
    tmp1 = tmp2 = 0
    prev = 'S'
    for dr in dartResult:
        if dr in 'SDT*#':
            if dr == 'S':
                tmp1 **= 1
            elif dr == 'D':
                tmp1 **= 2
            elif dr == 'T':
                tmp1 **= 3
            elif dr == '*':
                tmp1 *= 2
                tmp2 *= 2
            elif dr == '#':
                tmp1 *= -1
            prev = dr
        else:
            if str(prev) in 'SDT*#':
                answer += tmp2
                tmp1, tmp2, prev = int(dr), tmp1, int(dr)
            else:
                tmp1 = tmp1 * 10 + int(dr)
    answer += tmp1 + tmp2
    return answer

# print(solution('1S2D*3T'))
# print(solution('1D2S#10S'))
# print(solution('1D2S0T'))
print(solution('1S*2T*3S'))
print(solution('1D#2S*3S'))
print(solution('1T2D3D#'))
print(solution('1D2S3T*'))