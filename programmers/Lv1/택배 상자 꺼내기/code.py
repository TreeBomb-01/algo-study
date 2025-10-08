def solution(n, w, num):
    top=[]
    if n % w != 0:
        floor = (n // w) + 1
    else:
        floor = n // w
    
    for i in range(1,n+1,w):
        tmp=[j for j in range(i,i+w)]
        if len(top) % 2 != 0:
            tmp = list(reversed(tmp))
        top.append(tmp)
        if num in tmp:
            index = [len(top)-1,tmp.index(num)]
    
    print(index)
    answer = 0
    for i in reversed(top):
        if i[index[1]] <= n:
            answer+=1
            if i[index[1]] == num:
                return answer

    return answer