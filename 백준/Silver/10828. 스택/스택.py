import sys
q = []
for i in range(int(input())):
    s = sys.stdin.readline().rstrip().split()
    if s[0] == "pop":
        if len(q) > 0:
            print(q.pop())
        else:
            print(-1)
    elif s[0] == "size":
        print(len(q))
    elif s[0] == "empty":
        if len(q) > 0:
            print(0)
        else:
            print(1)
    elif s[0] == "top":
        if len(q) > 0:
            print(q[len(q)-1])
        else:
            print(-1)
    else:
        q.append((int(s[1])))