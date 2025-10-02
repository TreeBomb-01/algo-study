def solution(n, control):
    print(len(control))
    for i in range(len(control)):
        c = control[i:i+1]
        if c == "w":
            n+=1
        elif c == "a":
            n-=10
        elif c == "s":
            n-=1
        elif c == "d":
            n+=10
    return n
