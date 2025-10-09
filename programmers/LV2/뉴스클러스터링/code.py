import re
def solution(str1, str2):
    str1=str1.lower()
    str2=str2.lower()
    
    a = []
    b=[]
    for i in range(len(str1)-1):
        if list(str1)[i] >= "a" and list(str1)[i] <= "z":
            if list(str1)[i+1] >= "a" and list(str1)[i+1] <= "z":
                a.append(list(str1)[i] + list(str1)[i+1])
    for i in range(len(str2)-1):
        if list(str2)[i] >= "a" and list(str2)[i] <= "z":
            if list(str2)[i+1] >= "a" and list(str2)[i+1] <= "z":
                b.append(list(str2)[i] + list(str2)[i+1])
        
    if len(a) == 0 and len(b) == 0:
        return 65536
    
    print(a)
    print(b)
    
    print(set(a) & set(b))
    print(list(set(a) | set(b)))
    
    answer=(len(set(a) & set(b)) / len(set(a) | set(b))) * 65536

    return int(answer)