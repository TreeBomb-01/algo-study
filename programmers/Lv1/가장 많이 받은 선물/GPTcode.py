#GPT가 작성해준 코드임
def solution(friends, gifts):
    n = len(friends)
    idx = {name: i for i, name in enumerate(friends)}
    cnt = [[0]*n for _ in range(n)]
    sent = [0]*n
    recv = [0]*n

    # 기록 집계
    for g in gifts:
        a, b = g.split()
        ai, bi = idx[a], idx[b]
        cnt[ai][bi] += 1
        sent[ai] += 1
        recv[bi] += 1

    gift_index = [sent[i] - recv[i] for i in range(n)]
    next_recv = [0]*n

    # 각 쌍은 한 번만 (i < j)
    for i in range(n):
        for j in range(i+1, n):
            if cnt[i][j] > cnt[j][i]:
                next_recv[i] += 1
            elif cnt[i][j] < cnt[j][i]:
                next_recv[j] += 1
            else:
                # 동률 → 선물 지수 비교
                if gift_index[i] > gift_index[j]:
                    next_recv[i] += 1
                elif gift_index[i] < gift_index[j]:
                    next_recv[j] += 1
                # 같으면 아무도 안 받음

    return max(next_recv) if next_recv else 0
