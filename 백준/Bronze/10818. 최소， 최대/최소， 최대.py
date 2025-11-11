# int(input())
# li = list(map(int,input().split()))
# print(str(min(li))+" "+str(max(li)))
#------------------------------------------
len = int(input())
li = list(map(int,input().split()))
min=1000000
max=-1000000
for i in range(len):
    if li[i] < min:
        min = li[i]
    if li[i] > max:
        max = li[i]
print(str(min)+" "+str(max))