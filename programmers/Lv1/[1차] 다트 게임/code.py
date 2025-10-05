def solution(dartResult):
    li = list(dartResult)
    score=[0,0,0]
    n=0
    for i in range(len(dartResult)):
        if li[i] == "#":
            score[n-1] *= (-1)
        elif li[i] == "*":
            if n >= 1:
                score[n-1] *=2
                score[n-2] *=2
            else:
                score[n-1] *=2
        elif li[i] == "S":
            score[n]=(score[n])
            n+=1
        elif li[i] == "D":
            score[n]=(score[n]*score[n])
            n+=1
        elif li[i] == "T":
            score[n]=(score[n]*score[n]*score[n])
            n+=1
        elif li[i] == "0" and li[i-1] == "1":
            score[n]=10
        else:
            score[n]=int(li[i])

    return sum(score)