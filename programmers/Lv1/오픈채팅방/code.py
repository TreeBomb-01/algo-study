def solution(record):
    answer = []
    message=[]
    user={}
    
    for i in record:
        tmp = i.split(" ")
        if tmp[0] == "Enter" or tmp[0] == "Change":
            user[tmp[1]] = tmp[2]
            
        if tmp[0] == "Enter":
            message.append([tmp[1],"님이 들어왔습니다."])
        elif tmp[0] == "Leave":
            message.append([tmp[1],"님이 나갔습니다."])
    
    for i in message:
        answer.append(user[i[0]]+i[1])
        
    return answer