len, x = map(int,input().split())
li = list(map(int,input().split()))
answer=""
for i in li:
    if i < x:
        answer+=str(i) + " "
print(answer)
