def solution(n, w, num):
    # 전체 층 수(0-based로는 0..floor-1)
    floor = (n + w - 1) // w

    # num의 행/열(0-based)
    row = (num - 1) // w
    pos = (num - 1) % w
    # 지그재그이므로 층의 홀짝에 따라 열 계산
    col = pos if (row % 2 == 0) else (w - 1 - pos)

    # 같은 열로 위(꼭대기)까지 올라가며 존재하는 박스만 센다
    ans = 0
    for r in range(row, floor):
        # r층의 이 열에 실제 놓이는 번호 계산
        idx_in_row = col if (r % 2 == 0) else (w - 1 - col)
        box = r * w + idx_in_row + 1
        if box <= n:
            ans += 1

    return ans