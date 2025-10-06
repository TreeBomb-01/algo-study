# GPT-review: 성격 유형 검사 (Kakao) — 코드 리뷰

## ✅ 총평
- 전반적으로 **정확히 동작**하는 풀이입니다.  
- `score_map`과 역방향 문자열(예: `"TR" -> "RT"`)을 통해 **하나의 키셋**으로 정규화하는 아이디어가 좋습니다.  
- 최종 결정에서 **동점일 때 사전순(왼쪽 우선)** 규칙도 잘 지켰습니다 (`<= 0` 조건).

---

## 👍 잘한 점
1. **지표 통합 키(`RT/CF/JM/AN`) 사용**  
   - `"TR"` 같은 케이스를 뒤집어 같은 키로 관리 → 비교 로직 단순화.
2. **점수 테이블 분리(`score_map`)**  
   - 선택지에 따라 점수를 테이블로 분리해 가독성/수정 용이성 ↑
3. **동점 처리**  
   - `if not score["RT"] <= 0:` → `score["RT"] > 0`인 경우만 오른쪽 선택으로 바꾸므로, 동점(0)일 때 왼쪽 유지가 보장됨.

---

## 🤏 아쉬운 점 & 개선 포인트

### 1) 불필요한 인덱스 관리 (`n`) → `zip`으로 간결화 가능
현재:
```python
n = 0
for i in survey:
    # ...
    score[i] -= score_map[choices[n]]
    n += 1
```
개선:
```python
for s, c in zip(survey, choices):
    # s는 "RT"/"TR" 등, c는 선택지(1~7)
```

### 2) 조건식 가독성
```python
if not score["RT"] <= 0:
    answer[0] = "T"
```
보다 직관적으로:
```python
if score["RT"] > 0:
    answer[0] = "T"
```

### 3) 문자열 뒤집기 간결화
```python
i = list(i)
i.reverse()
i = "".join(i)
```
→ 파이썬스럽게 한 줄:
```python
i = i[::-1]
```

### 4) 자료형 모델을 더 단순하게 할 수 있음
- 현재는 `score_map` 부호(+/-)와 뒤집기 조합이 머릿속에서 역전되는 지점이 있어 **인지 부하**가 큼.
- **문자별 점수 누적**(예: `scores['R'] += ...`) 방식이 더 직관적이고 유지보수에 유리.

---

## 🛠️ 최소 수정 버전 (당신 코드 스타일 유지)
로직은 그대로 두고, 가독성과 파이썬스러움을 올린 버전입니다.

```python
def solution(survey, choices):
    answer = ["R", "C", "J", "A"]
    score = {"RT": 0, "CF": 0, "JM": 0, "AN": 0}  # 좌측 음수 / 우측 양수
    score_map = {1: 3, 2: 2, 3: 1, 4: 0, 5: -1, 6: -2, 7: -3}

    for s, c in zip(survey, choices):
        if s in score:
            score[s] -= score_map[c]
        else:
            s = s[::-1]              # "TR" -> "RT"
            score[s] += score_map[c]

    if score["RT"] > 0: answer[0] = "T"
    if score["CF"] > 0: answer[1] = "F"
    if score["JM"] > 0: answer[2] = "M"
    if score["AN"] > 0: answer[3] = "N"

    return "".join(answer)
```

- 변화점: `zip` 사용, 뒤집기 단축(`[::-1]`), 조건식 간결화.

---

## 🧭 정석/권장 버전 (문자별 누적)
각 문항 `"AB"`에 대해, 비동의(1~3)는 `A`에 `3/2/1`점, 동의(5~7)는 `B`에 `1/2/3`점 누적. 동점은 사전순(왼쪽).

```python
def solution(survey, choices):
    scores = {ch: 0 for ch in "RTCFJMAN"}
    points = [0, 3, 2, 1, 0, 1, 2, 3]  # index == 선택지

    for s, c in zip(survey, choices):
        a, b = s[0], s[1]       # 비동의쪽, 동의쪽
        if c < 4:               # 1, 2, 3
            scores[a] += points[c]
        elif c > 4:             # 5, 6, 7
            scores[b] += points[c]

    result = []
    for left, right in [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]:
        result.append(left if scores[left] >= scores[right] else right)

    return "".join(result)
```

### 장점
- **직관적** (어느 문자에 점수가 들어가는지 바로 보임)
- **부호 트릭/뒤집기 제거** → 버그 여지 감소
- 확장성/가독성 우수

---

## 🧪 간단 테스트
```python
print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]))  # TCMA
print(solution(["TR", "RT", "TR"], [7, 1, 3]))                    # RCJA
```

---

## 📌 요약
- 현재 코드 **정상 동작**하며 설계도 괜찮습니다.
- 다만, `zip`, `[::-1]`, 조건식 단순화 등으로 **가독성**을 높이고,  
  장기적으로는 **문자별 누적** 방식이 더 직관적이고 안전합니다.  
- 둘 다 코딩테스트에서 충분히 합격 가능한 수준입니다. 앞으로도 이 패턴 계속 가져가면 좋아요!
