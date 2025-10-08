def solution(bandage, health, attacks):
    t, x, y = bandage
    max_health = health

    cur = health       # 현재 체력
    streak = 0         # 연속 성공 시간(초)
    prev_time = 0      # 직전 공격 시각 (초). 시작은 0초 상태.

    for time, dmg in attacks:
        # 1) 직전 공격 이후 ~ 이번 공격 직전까지의 공백 시간
        gap = time - prev_time - 1
        if gap > 0 and cur > 0:
            # gap 동안의 회복량 계산 (수학적 누적)
            k = (streak + gap) // t         # 추가 회복 발생 횟수
            heal = gap * x + k * y
            cur = min(max_health, cur + heal)
            streak = (streak + gap) % t     # 다음 연속 카운터

        # 2) 이번 초에는 공격, 회복 없음 → 즉시 피해 적용
        cur -= dmg
        if cur <= 0:
            return -1

        # 3) 공격을 맞았으니 즉시 다시 사용, 카운터 리셋
        streak = 0
        prev_time = time

    # 모든 공격 직후의 체력 (추가 회복 없음)
    return cur