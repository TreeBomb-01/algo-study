n, k=map(int,input().split())
li = [i+1 for i in range(n)]
i = 0
answer = []
while len(answer) <= n-1:
    i = (i + k - 1) % len(li)
    answer.append(li.pop(i))

result = "<" + ", ".join(map(str, answer)) + ">"
print(result)