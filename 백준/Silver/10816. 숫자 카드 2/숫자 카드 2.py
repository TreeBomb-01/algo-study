import sys
from collections import Counter
_ = sys.stdin.readline().strip()
s = sys.stdin.readline().split()
_ = sys.stdin.readline().strip()
li = sys.stdin.readline().split()
result = [0 for _ in range(len(li))]
counts = dict(Counter(s))
for i in li:
    temp = counts.get(i)
    if temp == None:
        print(0 , end=" ")
    else:
        print(temp, end=" ")
