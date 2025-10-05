def solution(n, arr1, arr2):
    answer = []
    tmp=""
    for i in range(n):
        a = arr1[i] | arr2[i] #or연산자로 # 찾기
        if len(bin(a).split("b")[1]) != n:
            tmp = "0"+bin(a).split("b")[1]
        else:
            tmp = bin(a).split("b")[1]
        answer.append(tmp)
    final_map = []
    for i in answer:
        str=""
        for j in list(i):
            if j == '1':
                str += "#"
            else:
                str+=" "
        final_map.append(str)

        
            
    return final_map