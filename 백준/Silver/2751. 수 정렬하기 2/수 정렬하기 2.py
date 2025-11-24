import sys
input = sys.stdin.readline
l = int(input())
li=[]
for i in range(l):
    li.append(int(input()))

li = sorted(li)
for i in li:
    print(i)