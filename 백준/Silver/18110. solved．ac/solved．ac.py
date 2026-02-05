import math
import sys
n = int(input())
if n == 0:
    print(0)
else:
    s = math.floor(((n*(0.3))/2+0.5))
    li =[]
    for _ in range(n):
        li.append(int(sys.stdin.readline().rstrip()))
    li = sorted(li)
    if s > 0:
        print(math.floor(sum(li[s:-s])/(n-s*2)+0.5))
    else:
        print(math.floor((sum(li)/n)+0.5))