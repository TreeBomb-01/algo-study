from collections import Counter
import re

def solution(str1, str2):
    # 1️⃣ 소문자로 통일
    str1, str2 = str1.lower(), str2.lower()
    
    # 2️⃣ 알파벳만으로 이루어진 2글자씩 끊기
    a = [str1[i:i+2] for i in range(len(str1)-1) if re.match('[a-z]{2}', str1[i:i+2])]
    b = [str2[i:i+2] for i in range(len(str2)-1) if re.match('[a-z]{2}', str2[i:i+2])]
    
    # 3️⃣ 둘 다 공집합일 경우
    if not a and not b:
        return 65536
    
    # 4️⃣ Counter를 이용해 교집합 & 합집합 계산
    A, B = Counter(a), Counter(b)
    inter = sum((A & B).values())  # min
    union = sum((A | B).values())  # max
    
    # 5️⃣ 자카드 유사도 계산
    return int((inter / union) * 65536)
