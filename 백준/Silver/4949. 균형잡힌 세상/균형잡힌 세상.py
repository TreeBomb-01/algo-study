while True:
    li=[]
    result="yes"
    s = input()
    if s[0] == '.':
        break
    for i in s:
        if i == '(' or i == '[':
            li.append(i)
        elif i == ')':
            if not li or li.pop() != '(':
                result="no"
                break
        elif i == ']':
            if not li or li.pop() != '[':
                result="no"
                break
        elif i == '.':
            break
    if len(li) > 0:
        result="no"
    print(result)
        