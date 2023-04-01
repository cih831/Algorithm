import sys
sys.setrecursionlimit(10 ** 6)

def pre_order(in_s, in_e, post_s, post_e):
    if in_s > in_e or post_s > post_e:
        return
    
    root = post_order[post_e]

    left_node = node_num[root] - in_s
    right_node = in_e - node_num[root]

    print(root, end = " ")
    pre_order(in_s, in_s + left_node - 1, post_s, post_s + left_node - 1)
    pre_order(in_e - right_node + 1, in_e, post_e - right_node, post_e - 1)


N = int(input())

in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))

node_num = [0] * (N + 1)
for i in range(N):
    node_num[in_order[i]] = i

pre_order(0, N - 1, 0, N - 1)