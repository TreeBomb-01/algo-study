def solution(name, yearning, photo):
    answer = []
    p = {i : j for i,j in zip(name, yearning)}
    for i in photo:
        score=0
        for j in i:
            score+=p[j]
        answer.append(score)
    
        
    return answer

solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])