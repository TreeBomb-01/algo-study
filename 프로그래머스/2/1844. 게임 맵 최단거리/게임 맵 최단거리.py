from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dis = [[0]*m for i in range(n)]
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    queue = deque()
    queue.append((0,0))
    dis[0][0] = 1
    
    while queue:
        x,y = queue.popleft()
        
        if x == n-1 and y == m-1:
            return dis[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] == 1 and dis[nx][ny] == 0:
                    dis[nx][ny] = dis[x][y]+1
                    queue.append((nx,ny))
                    
    return -1
            
            
            
            