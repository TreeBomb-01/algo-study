from collections import deque
li = [i+1 for i in range(int(input()))]
li = deque(li)
while len(li) > 1:
    li.popleft()
    li.append(li.popleft())
print(li.pop())