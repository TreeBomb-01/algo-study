_ = int(input())
li = list(map(int,input().split()))
answer = 0
for i in li:
    isPrime = True
    if i < 2:
        isPrime = False
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            isPrime = False
    if isPrime: answer+=1

print(answer)