def solution(new_id):
    id_li = list(new_id.lower())
    for i in range(len(id_li)):
        if (int(id_li[i]) >= 97 and int(id_li[i]) <= 122) or (int(id_li[i]) >= 48 and int(id_li[i]) <=57) or id_li[i] == "-" or id_li[i] == "_" or id_li[i] == ".":
            if id_li[i] == "." and id_li[i+1]==".":
                id_li[i]=""
        else:
            id_li[i]=""
    
    if id_li[0] ==".":
        id_li.pop(0)
    elif id_li[len(id_li)-1] ==".":
        id_li.pop(len(id_li)-1)
    
    if len(id_li) == 0:
        id_li.append("a")
    if len(id_li) > 16:
        del id_li[14:]
        if id_li[len(id_li)-1] ==".":
            id_li.pop(len(id_li)-1)
    if len(id_li) <= 2:
        while len(id_li) >= 3:
            id_li.append(id_li[len(id_li)-1])
    
    print(id_li)

    answer = ''
    return answer

solution("...!@BaT#*..y.ABCDEfghijklm")