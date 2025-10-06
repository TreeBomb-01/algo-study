def solution(N, stages):
    stage=[] #실패한 사람
    stage_try=[] #시도 횟수
    fail={}
    answer = []
    for i in range(N):
        stage.append(0)
        stage_try.append(0)
    
    count=0
    for i in range(len(stage)):
        for j in stages:
            if i+1<=j:
                stage_try[i]+=1
            if i+1==j:
                stage[i]+=1
        fail[i+1]=(stage[i] / stage_try[i])

    for j in range(N):
        max = -1
        stage = 0
        for i in range(N):
            if i+1 in answer:
                pass
            elif max < fail[i+1]:
                max = fail[i+1]
                stage=i+1
        answer.append(stage)
        fail.pop(int(stage))
    
    return answer

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])