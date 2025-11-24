l = int(input())
li=[]
for i in range(l):
    x, y = input().split()
    li.append([x,y])

li = sorted(li, key=lambda li : (int(li[1]),int(li[0])))
for i in li:
    print(i[0],i[1])