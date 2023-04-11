# info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
#         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
# query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
#          "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
#          "- and - and - and chicken 100", "- and - and - and - 150"]
# answer = []
#
# for i in range(len(info)):
#     info[i] = list(info[i].split())
#     info[i][-1] = int(info[i][-1])
#
# info.sort(key=lambda x: x[-1])
#
# print(info)
#
# for condition in query:
#     lang, _, job, _, career, _, food, score = condition.split()
#     score = int(score)
#     cnt = 0
#     for idx in range(len(info)):
#         if (lang == '-' or lang == info[idx][0]) and (job == '-' or job == info[idx][1]) and (career == '-' or career == info[idx][2]) and (food == '-' or food == info[idx][3]) and info[idx][4] >= score:
#             cnt += 1
#     answer.append(cnt)
#
# print(answer)

info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150",
         "- and - and - and chicken 100", "- and - and - and - 150"]
answer = []

def bin_search(target, data):
    start = 0
    end = len(data) - 1
    if not end:
        return start

    while start <= end:
        mid = (start + end) // 2

        if data[mid][-1] == target:
            tmp = mid - 1
            while tmp and data[mid][-1] == data[tmp][-1]:
                tmp -= 1
            return tmp + 1
        elif data[mid][-1] < target:
            start = mid + 1
        else:
            end = mid - 1

    return start

for i in range(len(info)):
    info[i] = list(info[i].split())
    info[i][-1] = int(info[i][-1])

info.sort(key=lambda x: x[-1])
print(info)
for condition in query:
    lang, _, job, _, career, _, food, score = condition.split()
    score = int(score)
    cnt = 0
    s = bin_search(score, info)
    for idx in range(s, len(info)):
        if (lang == '-' or lang == info[idx][0]) and (job == '-' or job == info[idx][1]) and (career == '-' or career == info[idx][2]) and (food == '-' or food == info[idx][3]):
            cnt += 1
    answer.append(cnt)

print(answer)

# def bin_search(target, data):
#     start = 0
#     end = len(data) - 1
#     if not end:
#         return start
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if data[mid] == target:
#             return mid
#         elif data[mid] < target:
#             start = mid + 1
#         else:
#             end = mid - 1
#
#     return start
#
# a = [1, 2, 4, 4, 4, 4, 4, 4, 9, 10]
# print(bin_search(4, a))