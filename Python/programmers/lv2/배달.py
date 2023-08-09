def solution(N, road, K):
    from collections import deque
    answer = 1
    graph = [[] for _ in range(N + 1)]
    visited = [-1] * (N + 1)
    for r in road:
        graph[r[0]].append((r[1], r[2]))
        graph[r[1]].append((r[0], r[2]))
    q = deque()
    q.append(1)
    visited[1] = 0
    while q:
        now = q.popleft()
        for next, dist in graph[now]:
            if visited[now] + dist < visited[next]:
                visited[next] = visited[now] + dist
                q.append(next)
            elif visited[next] == -1 and visited[now] + dist <= K:
                visited[next] = visited[now] + dist
                q.append(next)
                answer += 1
    return answer

print(solution(
    5,
    [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],
    3
))