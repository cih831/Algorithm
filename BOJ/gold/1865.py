import sys

input = sys.stdin.readline
inf = int(1e9)

def bellman_ford(s):
    distance = [inf] * (N + 1)
    distance[s] = 0

    for i in range(N + 1):
        for edge in edges:
            cur_node, next_node, edge_cost = edge
            if distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                if i == N:
                    return "YES"
    
    return "NO"

TC = int(input())

for tc in range(TC):
    N, M, W = map(int, input().split())
    edges = []

    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    print(bellman_ford(1))