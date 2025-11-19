l = int(input())
t_l = list(map(int, input().split()))
t, p = map(int,input().split())
t_a = [0]*len(t_l)
for i in range(len(t_l)):
    x = t_l[i]
    t_a[i] += x // t
    if x % t != 0:
        t_a[i] += 1

print(sum(t_a))
print(l // p, l %p)
