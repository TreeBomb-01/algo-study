# README: 오픈채팅방 문제 풀이 코드 리뷰

## 1. 전반적인 평가
- 코드 구조가 단순하고 깔끔하며, 문제 요구사항을 정확히 충족합니다.  
- 특히 `Enter`/`Leave` 메시지를 **딕셔너리 매핑**으로 처리한 점이 인상적이었으며, Python에서 딕셔너리를 활용하는 방법을 자연스럽게 익힐 수 있습니다.  
- 전체적으로 흠잡을 부분이 거의 없는 좋은 코드입니다.

---

## 2. 코드의 장점
1. **최신 닉네임 반영**  
   - `Enter`/`Change` 시점마다 `namespace[uid] = nick`을 갱신하여, 과거 메시지까지 자동으로 최신 닉네임이 반영됩니다.

2. **메시지 문자열 매핑**  
   ```python
   printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
   ```
   - 조건문 대신 딕셔너리를 활용하여 중복 코드를 줄이고 가독성을 높였습니다.

3. **두 단계 처리 구조**  
   - 1차 루프: 닉네임 최신화  
   - 2차 루프: 최종 메시지 렌더링  
   - 문제 요구사항과 완전히 일치하는 접근입니다.

4. **시간/공간 효율성**  
   - 입력 크기 100,000에서도 O(N)으로 충분히 빠르게 동작합니다.

---

## 3. 개선할 수 있는 부분
1. **중복 split 호출 최적화**  
   ```python
   for r in record:
       if r.split(' ')[0] != 'Change':
           answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])
   ```
   - 같은 문자열을 세 번 `split`하는 것은 낭비입니다.  
   - 한 번만 쪼개서 변수에 담아 재사용하면 효율이 올라갑니다.

2. **네이밍 개선**  
   - `namespace` → `name` 혹은 `uid_to_name`  
   - 역할이 더 명확하게 드러납니다.

3. **split(' ') 대신 split()**  
   - `split()`은 연속 공백도 처리하므로 더 안전합니다.

---

## 4. 정리된 개선 버전 예시
```python
def solution(record):
    answer = []
    name = {}
    printer = {'Enter': '님이 들어왔습니다.', 'Leave': '님이 나갔습니다.'}

    # 닉네임 최신화
    for r in record:
        parts = r.split()
        cmd, uid = parts[0], parts[1]
        if cmd in ('Enter', 'Change'):
            name[uid] = parts[2]

    # 최종 메시지 출력
    for r in record:
        parts = r.split()
        cmd, uid = parts[0], parts[1]
        if cmd != 'Change':
            answer.append(name[uid] + printer[cmd])

    return answer
```

---

## 5. 학습 포인트
- Python에서 **딕셔너리**를 이용하면 조건문을 줄이고 코드 가독성을 높일 수 있다.  
- 데이터 전처리(닉네임 최신화)와 출력(메시지 생성)을 **두 단계로 나누는 사고**가 중요하다.  
- 작은 최적화(`split()` 재사용, 변수명 명확화)가 코드를 더 견고하고 읽기 쉽게 만든다.
