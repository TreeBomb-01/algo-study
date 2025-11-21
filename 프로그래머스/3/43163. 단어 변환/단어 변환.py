from collections import deque
def solution(begin, target, words):
    def check_one(a,b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
                if count == 2:
                    return False
        
        return count == 1
    
    answer = 0
    queue = deque()
    queue.append((begin,0))
    
    visited = set()
    visited.add(begin)
    
    while queue:
        n, c = queue.popleft()
        
        if n == target:
            return c
        
        for i in words:
            if i not in visited and check_one(n,i):
                visited.add(i)
                queue.append((i,c+1))
            
    return 0
            