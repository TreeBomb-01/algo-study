def solution(n, w, num):
    m1 = num%(w*2)
    m2 = ((w*2+1) - m1)%(w*2)
    # num 이상 n 이하의 수들 중 2*w로 나눈 나머지가 m1,m2인 것들의 수를 세면 된다.
    return len(range(num,n+1,w*2)) + len(range(num + (m2-m1)%(w*2), n+1, w*2))