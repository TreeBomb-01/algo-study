import sys
_ = int(input())
a = set(sys.stdin.readline().rstrip().split())
_ = int(input())
m = sys.stdin.readline().rstrip().split()

for i in m:
    if i in a:
        print(1)
    else:
        print(0)
