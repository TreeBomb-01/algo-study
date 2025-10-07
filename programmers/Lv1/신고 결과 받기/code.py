def solution(id_list, report, k):
    report_by={u: set() for u in id_list}
    report_cnt={u: 0 for u in id_list}

    for i in report:
        a,b = i.split(" ")
        if b in report_by[a]:
            continue
        report_by[a].add(b)
        report_cnt[b] += 1

    ban={u for u , i in report_cnt.items() if i>=k}

    answer=[]
    for i in id_list:
        cnt = sum(1 for target in report_by[i] if target in ban)
        answer.append(cnt)

    return answer


solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3)
solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)