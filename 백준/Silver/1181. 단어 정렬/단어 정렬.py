l = int(input())
li = {input() for _ in range(l)}
sorted_list = sorted(li, key=lambda x: (len(x), x))
for i in sorted_list:
    print(i)