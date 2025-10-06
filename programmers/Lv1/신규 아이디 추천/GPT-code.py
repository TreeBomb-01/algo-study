import re

def solution(new_id):
    s = new_id.lower()                               # 1
    s = re.sub(r'[^a-z0-9\-_.]', '', s)             # 2: 허용문자만
    s = re.sub(r'\.+', '.', s)                      # 3: 연속 '.' -> '.'
    s = s.strip('.')                                # 4: 양끝 '.'
    if not s:                                       # 5
        s = 'a'
    s = s[:15]                                      # 6-1: 15자 제한
    s = s.rstrip('.')                               # 6-2: 끝 '.' 제거
    while len(s) < 3:                               # 7
        s += s[-1]
    return s
