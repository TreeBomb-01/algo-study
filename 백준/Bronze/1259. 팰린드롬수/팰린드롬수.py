while True:
    n = int(input())
    if n == 0:
        break
    reversed_n = reversed(str(n))
    reversed_n = int("".join(reversed_n))
    if n == reversed_n:
        print("yes")
    else:
        print("no")