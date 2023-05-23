# deque의 인자로 maxlen을 사용하면 popleft를 사용할 필요가 없어짐!
# ex) deque(maxlen=cacheSize)

def solution(cacheSize, cities):
    from collections import deque

    answer = 0

    cache = deque(maxlen=cacheSize)
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
        if cities[i] in cache:                              # cache hit면 맨 뒤로 당겨줌
            # cache.remove(cities[i])
            cache.append(cities[i])
            answer += 1
        else:
            # if len(cache) == cacheSize: cache.popleft()     # cache miss면 맨 앞에꺼 지우고 추가해줌
            cache.append(cities[i])
            answer += 5
    # if not cacheSize:                                           # cacheSize 없으면 항상 cache miss
    #     answer = 5 * len(cities)
    # else:
    #     cache = deque()
    #     for i in range(len(cities)):
    #         cities[i] = cities[i].lower()
    #         if cities[i] in cache:                              # cache hit면 맨 뒤로 당겨줌
    #             cache.remove(cities[i])
    #             cache.append(cities[i])
    #             answer += 1
    #         else:
    #             if len(cache) == cacheSize: cache.popleft()     # cache miss면 맨 앞에꺼 지우고 추가해줌
    #             cache.append(cities[i])
    #             answer += 5

    return answer

print(solution(
    3,
    ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
))