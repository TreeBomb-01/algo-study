import sys
s = sys.stdin.readline().strip()
total = 0
target_w = 0
for i in range(13):
    w = 1 if i % 2 == 0 else 3
    if s[i] == "*":
        target_w = w
    else:
        total += int(s[i]) * w

for i in range(0,10):
    if (total + (i*target_w)) % 10 == 0:
        print(i)
        break