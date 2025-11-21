def solution(n, computers):
    answer = 0
    li = [False] * n
    
    def dfs(index):
        li[index] = True
        
        for j in range(n):
            if computers[index][j] == 1 and not li[j]:
                dfs(j)
        
        
    for i in range(n):
        if li[i] == False:
            print(i)
            dfs(i)
            answer += 1
            
    return answer
        
        
        
    