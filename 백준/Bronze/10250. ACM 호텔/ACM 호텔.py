l = int(input())
result=[]

for i in range(l):
    h,w,n = map(int,input().split())
    if n % h == 0:
        floar = h
        room = n // h
    else:
        floar = n % h
        room = n // h + 1
    result.append([floar,room])

for i in result:    
    print(f"{i[0]}{i[1]:02}")