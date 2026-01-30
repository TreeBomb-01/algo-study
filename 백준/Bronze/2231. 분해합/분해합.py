n = int(input())
start = max(1, n - len(str(n)) * 9)
answer=0

for m in range(start, n):
    digit_sum = sum(map(int, str(m)))
    
    if m + digit_sum == n:
        answer=m
        break
print(answer)