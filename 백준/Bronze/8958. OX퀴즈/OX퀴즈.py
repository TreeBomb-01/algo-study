l = int(input())
score = [0] * l
count = 1
for i in range(l):
    li = list(map(str, input().strip()))
    for j in li:
        if j == "O":
            score[i]+= count
            count += 1
        else:
            count = 1
    count = 1
for k in score:
    print(k)