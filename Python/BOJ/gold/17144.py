import sys

input = sys.stdin.readline


def dust():
    global graph
    graph_tmp = [[0] * C for _ in range(R)]
    graph_tmp[air_cleaner[0][0]][air_cleaner[0][1]] = -1
    graph_tmp[air_cleaner[1][0]][air_cleaner[1][1]] = -1
    for i in range(R):
        for j in range(C):
            if graph[i][j] > 0:
                cnt = 0
                tmp = graph[i][j] // 5
                for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] != -1:
                        graph_tmp[nx][ny] += tmp
                        cnt += 1
                graph_tmp[i][j] += graph[i][j] - tmp * cnt
    graph = graph_tmp


def refresh():
    global graph
    d = (((-1, 0), (0, 1), (1, 0), (0, -1)), ((1, 0), (0, 1), (-1, 0), (0, -1)))
    for cleaner_num in range(2):
        x, y, di = (
            air_cleaner[cleaner_num][0] + d[cleaner_num][0][0],
            air_cleaner[cleaner_num][1],
            0,
        )
        while True:
            nx, ny = x + d[cleaner_num][di][0], y + d[cleaner_num][di][1]
            if (
                (cleaner_num == 0 and not 0 <= nx <= air_cleaner[cleaner_num][0])
                or (cleaner_num == 1 and not air_cleaner[cleaner_num][0] <= nx < R)
                or not 0 <= ny < C
            ):
                di += 1
                nx, ny = x + d[cleaner_num][di][0], y + d[cleaner_num][di][1]
            if graph[nx][ny] != -1:
                graph[x][y], x, y = graph[nx][ny], nx, ny
            else:
                graph[x][y] = 0
                break


R, C, T = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(R)]

for i in range(R):
    if graph[i][0] == -1:
        air_cleaner = ((i, 0), (i + 1, 0))
        break

for _ in range(T):
    dust()
    refresh()


print(sum(sum(row) for row in graph) + 2)
