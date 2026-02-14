import sys
n = int(sys.stdin.readline().strip())
total = 1
for i in range(n):
    total*=n-i

c=0
while True:
    if total % 10 == 0:
        c+=1
        total=total // 10
    else:
        break

print(c)


''' 똑똑이 코드
# 사용자에게 N을 입력받음
n = int(input())

# 5의 배수의 개수 + 25의 배수의 개수 + 125의 배수의 개수
# (25는 5가 두 번, 125는 5가 세 번 들어있기 때문에 각각 더해주는 원리)
answer = (n // 5) + (n // 25) + (n // 125)

print(answer)
'''