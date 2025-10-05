def solution(dartResult):
    scores = []
    i = 0
    n = len(dartResult)

    while i < n:
        # 1) 점수 (0~10)
        if i + 1 < n and dartResult[i].isdigit() and dartResult[i + 1] == '0':
            num = 10
            i += 2
        else:
            num = int(dartResult[i])
            i += 1

        # 2) 보너스 S/D/T
        bonus = dartResult[i]
        i += 1
        if bonus == 'S':
            val = num ** 1
        elif bonus == 'D':
            val = num ** 2
        else:  # 'T'
            val = num ** 3

        # 3) 옵션 (* or #) — 있을 수도/없을 수도
        if i < n and dartResult[i] in ('*', '#'):
            opt = dartResult[i]
            i += 1
            if opt == '*':
                val *= 2
                if scores:              # 직전 라운드가 있으면 두 배
                    scores[-1] *= 2
            else:  # '#'
                val *= -1

        scores.append(val)

    return sum(scores)
