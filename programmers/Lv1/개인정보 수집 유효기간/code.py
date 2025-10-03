def date(start, term, today):
    yy,mm,dd = start.split(".")
    ty,tm,td = today.split(".")
    
    #오늘날짜 담길 변수
    ty = int(ty)
    tm = int(tm)
    td = int(td)
    
    today_day = ty*12*28 + (tm-1)*28 + td
    
    
    #계산후 날짜 담길 변수
    y = int(yy)
    m = int(mm)
    d= int(dd) - 1
    term = int(term)
    m = m + term
    
    ex_day = y*12*28 + (m-1)*28 + d
    
    if today_day > ex_day:
        return True
    else:
        return False
    
    
    

#모든 달은 28일까지라고 가정
def solution(today, terms, privacies):
    answer = []
    term_type=[]
    tbt=[] #term_by_type
    
    for i in terms: #terms 맵핑
        typ, tb = i.split(" ")
        term_type.append(typ)
        tbt.append(tb)
        
    n=1
    for i in privacies:
        start, typ = i.split(" ")
        term = tbt[term_type.index(typ)]
        yy,mm,dd = start.split(".")
        if date(start,term,today):
            #print(date)
            answer.append(n)
        n+=1            
            
        

        
    #print(term_type)
    #print(tbt)
    return answer