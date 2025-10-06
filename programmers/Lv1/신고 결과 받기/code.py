def solution(id_list, report, k):
    answer = []
    send_li={}
    req_list={}
    stop=[]
    for i in id_list:
        send_li[i]=[]
        req_list[i]=0
        answer.append(0)

    for i in report: #[0] 신고한 유저, [1] 신고당한 유저
        tmp = i.split(" ")
        if tmp[1] in send_li[tmp[0]]:
            pass
        else:
            send_li[tmp[0]].append(tmp[1])
            req_list[tmp[1]] += 1
            if req_list[tmp[1]] >= k:
                stop.append(tmp[1])

    print(stop)
    n=0
    for i in send_li:
        for j in stop:
            if j in send_li[i]:
                answer[n] += 1
        n+=1
        

    print(answer)
    return answer




solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3)
solution(["muzi", "frodo", "apeach", "neo"],["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],2)