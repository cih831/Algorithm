# LCS(Longest Common Subsequence, 최장 공통 부분 수열), 1차원 배열

import sys
input = sys.stdin.readline

word1, word2 = input().strip(), input().strip()
w1_len, w2_len = len(word1), len(word2)
cache = [0] * w2_len

for i in range(w1_len):
    cnt = 0
    for j in range(w2_len):
        if cnt < cache[j]:
            cnt = cache[j]
        elif word1[i] == word2[j]:
            cache[j] = cnt + 1

print(max(cache))