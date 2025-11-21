l = int(input())
li = list(map(int,input().split()))
m = max(li)
score = 0
for i in li:
    score += i/m*100
print(score/l)