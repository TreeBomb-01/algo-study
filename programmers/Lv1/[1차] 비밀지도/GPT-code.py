# 최소 수정 버전
def solution1(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = arr1[i] | arr2[i]                          # OR로 합치기
        bits = bin(a)[2:].zfill(n)                     # <-- n자리로 확실히 패딩
        row = []
        for ch in bits:
            row.append('#' if ch == '1' else ' ')
        answer.append(''.join(row))
    return answer

#python 스러운 버전
def solution2(n, arr1, arr2):
    return [
        ''.join('#' if c == '1' else ' ' for c in bin(arr1[i] | arr2[i])[2:].zfill(n))
        for i in range(n)
    ]