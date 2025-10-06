def solution(N, stages):
    # 1) 각 스테이지별 도전자 수 세기
    counts = [0] * (N + 2) # 0 안쓰고 1~N 스테이지 N+1 전부 클리어 -> N + 2(0,N+1)
    for s in stages:
        counts[s] += 1

    # 2) 실패율 계산
    result = []
    players = len(stages)  # 현재 도전자 수

    #전체 사용자 - 도전중인 사용자
    #첫 스테이지 - 도전중인 사용자 / 전체 사용자
    # -> 2번째 도달 사용자 = 전체 사용자 - 첫 스테이지 도전중인 사용자
    for i in range(1, N + 1):
        if players == 0:
            fail = 0
        else:
            fail = counts[i] / players
        result.append((i, fail))
        players -= counts[i]

    # 3) 실패율 내림차순, 스테이지 번호 오름차순 정렬
    result.sort(key=lambda x: (-x[1], x[0])) 
    #result[스테이즈, 실패율] -x[1] : 실패율을 기준으로 정렬, 실패율이 높은 스테이지부터 내림차순으로 하기 위해 - 부호
    #실패율이 같을경우 x[0]을 포함하여 정렬 

    return [i for i, _ in result]
