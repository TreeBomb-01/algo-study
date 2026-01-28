i = int(input())
for i in range(i):
    answer=0
    l = []
    a, b = input().split()
    li = list(input().split())
    for j in range(int(a)):
        l.append([int(li[j]),j])
    
    while True:
        t = True
        n = l.pop(0)
        for j,_ in l:
            if n[0] < j:
                l.append(n)
                t = False
                break
        if t:
            answer += 1
            if int(n[1]) == int(b):
                print(answer)
                break