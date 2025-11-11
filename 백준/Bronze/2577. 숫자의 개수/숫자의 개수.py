dict_values = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
a = int(input())
b = int(input())
c = int(input())
for i in str(a*b*c).strip():
    dict_values[int(i)] += 1

for i in dict_values.values():
    print(i)
