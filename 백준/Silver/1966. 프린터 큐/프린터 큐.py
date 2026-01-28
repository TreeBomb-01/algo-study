from collections import deque

i = int(input())
for i in range(i):
    answer=0
    l = []
    a, b = input().split()
    li = list(input().split())
    for j in range(int(a)):
        l.append([int(li[j]),j])
    l = deque(l)
    while True:
        t = True
        #print(l,t)
        n = l.popleft()
        for j,_ in l:
            if n[0] < j:
                l.append(n)
                t = False
                break
        if t:
            answer += 1
            #print(n[1]," == ", b, " ", n[1]==b)
            if int(n[1]) == int(b):
                print(answer)
                break