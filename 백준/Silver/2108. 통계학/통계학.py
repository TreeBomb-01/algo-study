import math
import sys
n = int(sys.stdin.readline().strip())
li = []
count_li=dict()
for _ in range(n):
    num = int(sys.stdin.readline().strip())
    li.append(num)
    if count_li.get(num) == None:
        count_li[num]=1
    else:
        count_li[num]=count_li.get(num)+1

print(math.floor((sum(li)/n)+0.5)) #산술평균 1번째 출력
sorted_li = sorted(li)
print(sorted_li[len(li)//2]) #중앙 2번째 출력

max_count = 0

count_li = dict(sorted(count_li.items(), key = lambda x : (-x[1], x[0])))

for i in count_li:
    if max_count == 0:
        min = i
        max_count = count_li.get(i)
    elif count_li.get(i) < max_count:
        break
    elif count_li.get(i) == max_count:
        min = i
        break
print(min)


# 첫 끝 차이 4번째 출력
if len(sorted_li) > 1:
    print(sorted_li[len(sorted_li)-1] - sorted_li[0])
else:
    print(0)
        