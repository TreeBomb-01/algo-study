len = int(input())
li = list(map(int,input().split()))
n = int(input())
answer=0
for i in li:
    if i == n:
        answer += 1
        
print(answer)