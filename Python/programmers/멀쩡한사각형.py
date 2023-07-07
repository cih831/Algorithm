def solution(w,h):
    from math import gcd
    d = gcd(w, h)
    return w * h - (w // d + h // d - 1) * d

print(solution(8, 12))