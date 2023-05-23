def solution(m, musicinfos):

    def trans(melody):                                      # 치환
        big = ['C#', 'D#', 'F#', 'G#', 'A#']
        small = ['c', 'd', 'f', 'g', 'a']
        for i in range(5):
            melody = melody.replace(big[i], small[i])
        return melody

    answer = '(None)'
    time_max = -1
    m = trans(m)
    for info in musicinfos:
        s, e, name, music = info.split(',')
        music = trans(music)
        s_HH, s_MM = map(int, s.split(':'))
        e_HH, e_MM = map(int, e.split(':'))
        time = (e_HH - s_HH) * 60 + e_MM - s_MM             # 방송 시간 계산
        music = ((time // len(music) + 1) * music)[:time]   # 노래보다 방송시간이 짧은 경우를 고려
        # if m in music and not (m + '#') in music and time > time_max:
        if m in music and time > time_max:                  # 들은 내용이 방송됐었고, 방송 시간이 원래 들었던 것보다 길면 교체
            answer = name
            time_max = time

    return answer

print(solution(
    "CCB",
    ["03:00,03:10,FOO,CCB#CCB", "04:00,04:08,BAR,ABC"]
))