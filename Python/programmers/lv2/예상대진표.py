def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()

print(solution(2, 1, 2))
print(solution(8, 3, 7))
print(solution(8, 7, 8))
print(solution(128, 84, 101))

"""
1번 선수가 첫째 자리이기 때문에 해당 자리를 0으로 표현하기 위해 -1 해줌
1, 2, 3, 4, 5, 6, 7, 8
0, 1, 10, 11, 100, 101, 110, 111

xor 연산을 취해주면 같은 자리의 숫자가 같으면 0이 되므로
같이 속하는 section을 걸러줄 수 있음

남은 길이를 return
"""
# print(bin(83), bin(100))
# print(bin(83^100))
# print()
# print(bin(83), bin(84))
# print(bin(83^84))
