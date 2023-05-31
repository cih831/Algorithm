def solution(m, n, board):
    answer = -1
    graph = [list(item) for item in board]
    tmp_ans = 0
    while answer != tmp_ans:
        answer = tmp_ans
        del_lst = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if graph[i][j] and graph[i][j] == graph[i + 1][j] == graph[i][j + 1] == graph[i + 1][j + 1]:
                    del_lst |= {(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)}

        for i in range(m, -1, -1):
            for j in range(n):
                if (i, j) in del_lst:
                    graph[i][j] = None
                    del_lst.discard((i, j))
                    tmp_ans += 1
                else:
                    i_tmp = i + 1
                    while i_tmp < m and not graph[i_tmp][j]:
                        graph[i_tmp][j], graph[i_tmp - 1][j] = graph[i_tmp - 1][j], None
                        i_tmp += 1

    return answer

print(solution(
    4,
    5,
    ["CCBDE", "AAADE", "AAABF", "CCBBF"]
))