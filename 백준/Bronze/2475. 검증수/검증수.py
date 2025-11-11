li=list(map(int,input().split()))
result=0
for i in li:
    result+=pow(i,2)
print(result%10)