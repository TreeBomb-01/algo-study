while True:
    x,y,z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break
    sort = sorted([x,y,z])
    if sort[0]**2 + sort[1]**2 == sort[2]**2:
        print("right")
    else:
        print("wrong")