import sys
len = int(input())

for i in range(len):
    a , b =map(int, sys.stdin.readline().split())
    print(a+b)