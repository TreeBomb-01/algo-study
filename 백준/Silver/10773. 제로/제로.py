answer = []
for i in range(int(input())):
    n = int(input())
    if n != 0:
        answer.append(n)
    else:
        answer.pop()

print(sum(answer))