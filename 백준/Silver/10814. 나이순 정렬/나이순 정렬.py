l = int(input())
li=[]
for i in range(l):
    age, name = input().split()
    li.append([int(age), name, i])

li.sort()

li.sort(key=lambda li : (li[0], li[2]))
for a, b, _ in li:
    print(a, b)
