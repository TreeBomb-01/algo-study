l = int(input())
li = []
for i in range(l):
    x, y = map(int, input().split())  # 정수로 변환
    li.append([x, y])

li = sorted(li, key=lambda v: (v[0], v[1]))

for i in li:
    print(i[0], i[1])
