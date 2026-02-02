i = int(input())
for i in range(i):
    k = int(input())
    n = int(input()) + 1
    total = []
    for j in range(k):
        li=[]
        for l in range(1,n):
            if j == 0:
                li.append(l)
            else:
                li.append(sum(total[j-1][0:l]))
        total.append(li)
    print(sum(total[k-1]))
