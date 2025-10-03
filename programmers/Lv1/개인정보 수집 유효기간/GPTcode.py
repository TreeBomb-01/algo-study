def to_days(date_str: str) -> int:
    """
    'YYYY.MM.DD' -> 문제 규칙(모든 달 = 28일)에 따른 절대 일수로 변환
    예) y*12*28 + (m-1)*28 + d
    """
    y, m, d = map(int, date_str.split("."))
    return y * 12 * 28 + (m - 1) * 28 + d


def solution(today, terms, privacies):
    # 1) today를 절대 일수로
    today_days = to_days(today)

    # 2) 약관 기간 맵 (ex: {'A': 6, 'B': 12, ...})
    term_months = {}
    for t in terms:
        kind, months = t.split()
        term_months[kind] = int(months)

    # 3) 각 개인정보의 만료일 계산 후, 오늘 기준 파기 대상(오늘 > 만료일)만 수집
    answer = []
    for idx, p in enumerate(privacies, start=1):
        start_date, kind = p.split()
        collected = to_days(start_date)

        # 만료일 = 수집일 + (약관개월 * 28일) - 1
        expire = collected + term_months[kind] * 28 - 1

        # 오늘이 만료일보다 크면 파기 대상
        if today_days > expire:
            answer.append(idx)

    return answer
