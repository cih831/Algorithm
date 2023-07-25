def solution(brown, yellow):
    area = brown + yellow
    for i in range(area // 2 + 1, 0, -1):
        if not area % i:
            w, h = i, area // i
            if 2 * w + 2 * (h - 2) == brown:
                return [w, h]

print(solution(10, 2))