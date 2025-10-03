def solution(friends, gifts):
    gift = [] #받을 선물
    name = [] #친구 리스트
    gift_c = [] #보낸 선물
    for i in friends:
        gift.append(0)
        friends_list = []
        for j in friends:
            friends_list.append(0)
        name.append(i)
        gift_c.append(friends_list)
            
    for i in gifts:
        p = i.split(" ")
        send = name.index(p[0])
        take = name.index(p[1])
        c = gift_c[send][take] + 1
        gift_c[send][take] = c
        
    for i in range(len(gift_c)): #A = i, B = j
        for j in range(len(gift_c)):
            if i!=j:
                if gift_c[i][j] > gift_c[j][i]: #선물 횟수 비교 1:1
                    gift[i] += 1
                elif gift_c[i][j] == gift_c[j][i]: # 같을 때
                    i_g=0
                    i_t=0
                    j_g=0
                    j_t=0
                    for k in range(len(gift_c)):
                        i_g += gift_c[k][i]
                        i_t += gift_c[i][k]
                        j_g += gift_c[k][j]
                        j_t += gift_c[j][k]
                    gsu_i = i_t - i_g
                    gsu_j = j_t - j_g
                    if gsu_i > gsu_j:
                        gift[i] += 1
                    elif gsu_i < gsu_j:
                        gift[j] += 1               
                else:
                    gift[j] += 1
                    
    max = 0
    for i in gift:
        if max < i:
            max = i

    answer = 0
    return max/2