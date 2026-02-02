_ , m = input().split()
li = list(map(int,input().split()))
m = int(m)

def r(li,m):
    total = 0
    now=9999999
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            for k in range(j+1,len(li)):
                s = li[i]+li[j]+li[k]
                if s == m:
                    return s
                elif s < m:
                    a = m-s
                    if a < now:
                        total = s
                        now = a
    return total

print(r(li,m))