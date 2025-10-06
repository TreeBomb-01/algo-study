def solution(new_id):
    answer = ''
    id_li = list(new_id.lower())

    for i in range(len(id_li)):
        if (ord(id_li[i]) >= 97 and ord(id_li[i]) <= 122) or (ord(id_li[i]) >= 48 and ord(id_li[i]) <=57) or id_li[i] == "-" or id_li[i] == "_" or id_li[i] == ".":
            pass
        else:
            id_li[i]=""
        answer += id_li[i]
    
    id_li = list(answer)
    for i in range(len(id_li)-1):
        if id_li[i] == "." and id_li[i+1]==".":
                id_li[i]=""
    
    answer = ""
    for i in id_li:
        answer += i
    id_li = list(answer)
    
    print(id_li)
    
    if id_li[0] ==".":
        id_li.pop(0)
    elif id_li[len(id_li)-1] ==".":
        id_li.pop(len(id_li)-1)
    
    if len(id_li) == 0:
        id_li.append("a")
    if len(id_li) >= 16:
        del id_li[15:]
        if id_li[len(id_li)-1] ==".":
            id_li.pop(len(id_li)-1)
    if len(id_li) < 3:
        while len(id_li) < 3:
            id_li.append(id_li[len(id_li)-1])
    
    
    answer = ""
    for i in id_li:
        answer += i
    
    print(answer)
    return answer
    

solution("...!@BaT#*..y.abcdefghijklm")