s = list(map(str,input().strip()))
result = [-1]*26

n=97

for i in range(len(s)):
    a = ord(s[i]) - 97
    if result[a] == -1:
        result[a] = i

for i in result:
    print(i, end=' ')
