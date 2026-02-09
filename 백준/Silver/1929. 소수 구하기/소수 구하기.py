import sys
import math
a, b = map(int, sys.stdin.readline().split())

for i in range(a,b+1):
    bo=True
    if i == 2:
        print(2)
    elif i % 2 == 0 or i == 1:
        pass
    else:
        for j in range(2,int(math.sqrt(i))+1):
            if i % j == 0:
                bo=False
                break
        if bo:
            print(i)            
