pado = [0] * 101
pado[1], pado[2], pado[3], pado[4], pado[5], pado[6], pado[7], = 1, 1, 1, 2, 2, 3, 4
for i in range(8, 101):
    pado[i] = pado[i-1] + pado[i-5]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print(pado[N])