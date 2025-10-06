def solution(id_list, report, k):
    # 1) 중복 신고 제거
    unique = set(report)

    # 2) 자료구조 준비
    reported_by = {u: set() for u in id_list}  # 신고자 -> (신고 대상들)
    reported_cnt = {u: 0 for u in id_list}     # 피신고자 -> 신고당한 횟수

    # 3) 집계
    for rec in unique:
        a, b = rec.split()
        if b in reported_by[a]:
            continue
        reported_by[a].add(b)
        if b in reported_cnt:     # 안전 guard
            reported_cnt[b] += 1

    # 4) 정지 유저
    suspended = {u for u, c in reported_cnt.items() if c >= k}

    # 5) 메일 카운트 (id_list 순서)
    answer = []
    for u in id_list:
        cnt = sum(1 for target in reported_by[u] if target in suspended)
        answer.append(cnt)
    return answer
