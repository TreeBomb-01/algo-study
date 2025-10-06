def solution(survey, choices):
    # 각 성격 문자 점수 테이블
    scores = {ch: 0 for ch in "RTCFJMAN"}
    points = [0, 3, 2, 1, 0, 1, 2, 3]  # idx=선택지(1~7)

    for s, c in zip(survey, choices):
        a, b = s[0], s[1]  # 비동의쪽, 동의쪽
        if c < 4:          # 비동의 선택
            scores[a] += points[c]
        elif c > 4:        # 동의 선택
            scores[b] += points[c]

    # 지표별로 점수 비교 (동점이면 사전순)
    result = []
    for left, right in [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]:
        result.append(left if scores[left] >= scores[right] else right)

    return "".join(result)
