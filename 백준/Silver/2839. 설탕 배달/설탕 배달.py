n = int(input())
li = []
t = n // 3
f = n // 5
for i in range(1,t+1):
    temp = n-3*i
    if temp % 5 == 0:
        li.append(i+(temp//5))
for i in range(1,f+1):
    temp = n-5*i
    if temp % 3 == 0:
        li.append(i+(temp//3))
if len(li) == 0:
    print(-1)
else:
    print(min(li))