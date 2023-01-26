N = int(input())
number = list(map(int,input().split()))

my_max = number[0]
my_min = number[0]

for i in range(N):
    if number[i] > my_max:
        my_max = number[i]
    elif number[i] < my_min:
        my_min = number[i]

print(my_min, my_max)