n = int(input())
for i in range(n):
    open=0
    result="YES"
    li=input().strip()
    if len(li)%2 == 1:
        print("NO")
    else:
        for c in li:
            if c == '(':
                open+=1
            else:
                open-=1
            
            if open < 0:
                result="NO"
                break

        if open > 1:
            result="NO"
        print(result)