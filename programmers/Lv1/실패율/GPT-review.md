# GPT-review: 실패율 문제 코드 리뷰

## 1) 전반 평가
사용자의 코드는 실패율 계산 로직을 명확히 구현하려는 의도는 좋지만, **시간 복잡도(O(N×len(stages)))**와 **런타임 에러 가능성** 때문에 비효율적입니다.  
특히 대규모 입력(`stages` 최대 200,000, `N` 최대 500)에서 **중첩 루프**로 인해 시간 초과가 발생합니다.

---

## 2) 현재 코드의 구조적 문제점

### ① 중첩 루프 구조
```python
for i in range(len(stage)):
    for j in stages:
        if i+1 <= j:
            stage_try[i] += 1
        if i+1 == j:
            stage[i] += 1
```
- 매 스테이지(`N`)마다 모든 유저(`len(stages)`)를 순회 → 최악의 경우 **500 × 200,000 = 1억 회 연산**.
- Python에서는 이 정도면 **시간 초과 확정적**입니다.

✅ **개선 방향:**  
한 번의 순회로 각 스테이지별 도전/실패 인원을 집계할 수 있습니다.  
(`collections.Counter` 또는 단순 배열 누적)

---

### ② 런타임 에러 가능성
```python
fail[i+1] = (stage[i] / stage_try[i])
```
- `stage_try[i] == 0`인 경우 `ZeroDivisionError` 발생 가능.
- 문제 조건에서 “스테이지에 도달한 유저가 없는 경우 실패율 = 0”이므로 예외처리 필요.

✅ **개선 방향:**
```python
fail[i+1] = stage[i] / stage_try[i] if stage_try[i] != 0 else 0
```

---

### ③ 변수명 충돌 및 혼동
- `stage` 변수가 리스트이면서 후반부에서 `stage = 0`으로 재정의됨 → 가독성 저하 및 잠재적 오류.

✅ **개선 방향:**
`stage_fails`, `stage_reaches`, `fail_rates` 같은 **의미 있는 변수명**을 사용하는 것이 좋습니다.

---

### ④ 불필요한 최대 탐색 반복
```python
for j in range(N):
    max = -1
    stage = 0
    for i in range(N):
        if i+1 in answer:
            pass
        elif max < fail[i+1]:
            max = fail[i+1]
            stage = i+1
    answer.append(stage)
    fail.pop(int(stage))
```
- 매번 `N`개를 반복해 `max`를 찾는 구조 → 정렬 대신 수동 탐색 → 비효율적(O(N²)).

✅ **개선 방향:**
`sorted()`로 한 번에 정렬:
```python
sorted_fail = sorted(fail.items(), key=lambda x: (-x[1], x[0]))
answer = [s for s, _ in sorted_fail]
```

---

## 3) 정석 풀이

```python
def solution(N, stages):
    # 1) 각 스테이지별 도전자 수 세기
    counts = [0] * (N + 2)
    for s in stages:
        counts[s] += 1

    # 2) 실패율 계산
    result = []
    players = len(stages)  # 현재 도전자 수

    for i in range(1, N + 1):
        if players == 0:
            fail = 0
        else:
            fail = counts[i] / players
        result.append((i, fail))
        players -= counts[i]

    # 3) 실패율 내림차순, 스테이지 번호 오름차순 정렬
    result.sort(key=lambda x: (-x[1], x[0]))

    return [i for i, _ in result]
```

---

## 4) 개선 포인트 요약

| 항목 | 기존 코드 | 개선 방향 |
|------|------------|------------|
| 시간 복잡도 | O(N×len(stages)) | O(N + len(stages)) |
| 실패율 계산 | ZeroDivisionError 가능 | 조건문으로 예외처리 |
| 변수 관리 | `stage` 중복 사용 | 명확한 변수명 분리 |
| 정렬 로직 | 수동 최대 탐색 | `sorted()` 내장 함수 사용 |
| 메모리 | 다소 낭비 | `N+2` 크기의 배열로 충분 |

---

## 5) 결론
- **로직 아이디어는 옳음** (실패율 = 실패 / 도전).  
- **성능과 안정성**이 부족해 실제 대규모 입력에서는 실행 불가.
- 정석 풀이처럼 **누적 방식 + 정렬 한 번**으로 개선하면 시간 초과와 런타임 에러 모두 해결됩니다.
