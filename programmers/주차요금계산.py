from math import ceil

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
answer = []

d = {}
cars = set()

for rec in records:                                  # 차량별 입출입 시간 정리
    time, num, action = rec.split()
    cars.add(num)
    if not num in d:
        d[num] = [time]
    else:
        d[num].append(time)

cars = sorted(list(cars))

for car in cars:                                     # 주차 시간 계산
    tmp = 0
    for i in range(0, len(d[car]) - 1, 2):
        HH, MM = map(int, d[car][i].split(':'))
        car_in = HH * 60 + MM
        HH, MM = map(int, d[car][i + 1].split(':'))
        car_out = HH * 60 + MM
        tmp += car_out - car_in
    if len(d[car]) % 2:                              # 마지막에 입차만 있는 경우
        HH, MM = map(int, d[car][-1].split(':'))
        tmp += (23 * 60 + 59) - (HH * 60 + MM)

    if tmp < fees[0]:
        answer.append(fees[1])
    else:
        answer.append(fees[1] + ceil((tmp - fees[0])/fees[2]) * fees[3])

print(answer)