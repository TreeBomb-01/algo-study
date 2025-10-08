def solution(bandage, health, attacks):
    #print(attacks[len(attacks)-1][0])
    max_health = health
    answer = 0
    attack = { i : j for i, j in attacks}
    print(attack)
    sec = {i : [health,0] for i in range(attacks[len(attacks)-1][0]+1)}
    for i in range(1,len(sec)):
        if i in attack:
            health, _ = sec[i-1]
            if health - attack[i] <= 0:
                return -1
            sec[i] = [health-attack[i],0]
        else:
            health, j = sec[i-1]
            if bandage[0]-1 <= j:
                health=health+bandage[1]+bandage[2]
                j=0
                sec[i] = [health,j]
            else:
                health+=bandage[1]
                j+=1
                sec[i] = [health,j]
            if health > max_health:
                sec[i] = [max_health,j]
                  
    print(sec)
    
    return sec[len(sec)-1][0]


solution([5, 1, 5],30,[[2, 10], [9, 15], [10, 5], [11, 5]])