def solution(n, words):
    s = set()
    s.add(words[0])
    tmp = words[0]
    for i in range(1, len(words)):
        print(i, words[i], tmp[-1], words[i][0], s)
        s.add(words[i])
        if tmp[-1] != words[i][0] or len(s) != i + 1:
            return [(i + 1) % n if (i + 1) % n else n, (i + 1) // n + 1 if (i + 1) % n else (i + 1) // n]
        tmp = words[i]

    return [0, 0]

print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"]))