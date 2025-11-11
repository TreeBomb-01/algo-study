li=list(map(int,input().split()))
if li[0]==8:
    result="descending"
elif li[0]==1:
    result="ascending"
else:
    result="mixed"
if result!="mixed":
    for i in range(1,8):
        if result=="ascending" and li[i]-li[i-1]!=1:
            result="mixed"
            break
        elif result=="descending" and li[i]-li[i-1]!=-1:
            result="mixed"
            break
print(result)