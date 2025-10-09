def solution(m, n, board):
    index = []
    for i in board:
        print(i)
    for i in range(m-2):     
        for j in range(n-1):
            c = board[i][j]
            tmp = []
            if c == board[i][j+1] and c == board[i+1][j] and c == board[i+1][j+1]:
                index.append([i,j])
                index.append([i+1,j])
                index.append([i,j+1])
                index.append([i+1,j+1])
                #index.append(tmp)
    for i in index:
        print(set(index))
        
    answer = 0
    return answer

solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])