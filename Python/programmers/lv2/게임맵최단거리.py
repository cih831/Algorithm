def solution(maps):
    from collections import deque
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1
    q = deque()
    q.append((0, 0))
    while q:
        x, y = q.popleft()
        if x + y == m + n - 2:
            break
        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
    return visited[n - 1][m - 1] if visited[n - 1][m - 1] else -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))