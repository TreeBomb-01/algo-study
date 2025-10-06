def solution(survey, choices):
    answer = ["R","C","J","A"]
    score={"RT":0,"CF":0,"JM":0,"AN":0} #좌측 -> 음수, 우측 -> 양수
    score_map={1:3,2:2,3:1,4:0,5:-1,6:-2,7:-3}
    n=0
    for i in survey:
        if i in score:
            score[i]-=score_map[choices[n]]
        else:
            i = list(i)
            i.reverse()
            i="".join(i)
            score[i]+=score_map[choices[n]]
        n+=1

    if not score["RT"] <= 0:
        answer[0]="T"
    if not score["CF"] <= 0:
        answer[1]="F"
    if not score["JM"] <= 0:
        answer[2]="M"
    if not score["AN"] <= 0:
        answer[3]="N"
    
    return "".join(answer)

solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5])