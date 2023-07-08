# # 비트 연산자
# print(bin(0b1010 & 0b1111))  # and   &: 대응하는 두 비트가 모두 1일 때, 1 반환
# print(bin(0b1010 | 0b1111))  # or    |: 대응하는 두 비트가 하나라도 1일 때, 1 반환
# print(bin(0b1010 ^ 0b1111))  # xor   ^: 대응하는 두 비트가 서로 다를 때, 1 반환
# print(bin(~0b00001111))  # not   ~: 비트의 값을 반전하여 반환

# # Shift
# print(bin(0b1010 << 2))
# print(bin(0b1010 >> 2))

# import sys

# input = sys.stdin.readline

# M = int(input())
# S = 0
# for _ in range(M):
#     command = input().strip().split()
#     if command[0] == "all":
#         S = (1 << 20) - 1
#     elif command[0] == "empty":
#         S = 0
#     else:
#         command, x = command[0], int(command[1]) - 1

#         if command == "add":
#             S |= 1 << x
#         elif command == "remove":
#             S &= ~(1 << x)
#         elif command == "check":
#             print(1 if S & (1 << x) != 0 else 0)
#         elif command == "toggle":
#             S ^= 1 << x

"""
A, B
A & B
A | B
A ^ B
"""


def bitCount(x):
    if not x:
        return 0
    return x % 2 + bitCount(x // 2)

mask = 0xf
print(bin(5 & mask))
print(bin(-5 & mask))
print(bin(10 & mask))
print(bin(-10 & mask))
print(bin(7))
print(bin(~7))
print(bin(0b100 + 0b100))