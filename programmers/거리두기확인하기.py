def solution(places):
    from collections import deque
    answer = []
    for place in places:
        arr = [list(status) for status in place]
        flag = 1
        visited = [[-1] * 5 for _ in range(5)] # 사람간 거리

        # BFS
        for i in range(5):
            for j in range(5):
                if arr[i][j] == 'P' and visited[i][j] == -1:
                    q = deque()
                    q.append((i, j))
                    visited[i][j] = 0
                    while q and flag:
                        x, y = q.popleft()
                        for dx, dy in (1, 0), (0, 1), (-1, 0), (0, -1):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < 5 and 0 <= ny < 5 and arr[nx][ny] != 'X' and visited[nx][ny] == -1:
                                q.append((nx, ny))
                                visited[nx][ny] = visited[x][y] + 1
                                if arr[nx][ny] == 'P': # 사람 찾으면 거리두기를 지키고 있다면 거리를 0으로 초기화
                                    if visited[nx][ny] <= 2: flag = 0
                                    else: visited[nx][ny] = 0
        answer.append(flag)
        
    return answer

print(solution(
    [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
     ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
     ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
     ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
     ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
))