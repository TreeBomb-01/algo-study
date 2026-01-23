def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n, k = map(int,input().split())
if k == 0:
    print(1)
else:
    nf = factorial(n)
    kf = factorial(k)
    nkf = factorial(n-k)

    print(int(nf/(kf*nkf)))