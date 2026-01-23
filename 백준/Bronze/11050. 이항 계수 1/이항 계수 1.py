def factorial_for(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n, k = map(int,input().split())
if k == 0:
    print(1)
else:
    nf = factorial_for(n)
    kf = factorial_for(k)
    nkf = factorial_for(n-k)

    print(int(nf/(kf*nkf)))