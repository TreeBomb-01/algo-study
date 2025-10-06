# GPT-review: 신고 결과 받기 (카카오) — 코드 리뷰

## 1) 무엇이 문제였나?

### A. `stop`을 리스트로 관리 → **중복 추가 + 과도한 연산**
```python
if req_list[tmp[1]] >= k:
    stop.append(tmp[1])   # 동일 유저가 k 이상일 때마다 계속 append됨
```
- 같은 유저가 여러 번 기준을 넘을 때 **중복으로** 들어갑니다.
- 이후
```python
for i in send_li:
    for j in stop:
        if j in send_li[i]:
            answer[n] += 1
```
- `stop`의 **중복 길이만큼** 불필요하게 반복하며, `in`도 리스트에서 O(len) → **시간 폭탄**.

**대책**: `stop`을 **set**으로 관리해 **유일성** 보장 + membership O(1).

---

### B. 신고 중복 체크를 리스트로 → O(M) 탐색
```python
if tmp[1] in send_li[tmp[0]]:   # send_li[신고자]가 리스트
    pass
else:
    send_li[tmp[0]].append(tmp[1])
```
- 같은 신고자-피신고자 쌍 중복 여부 확인이 리스트면 O(리스트 길이).
- report가 최대 20만이므로 **누적 비용 커짐**.

**대책**: `send_li[신고자]`를 **set**으로 관리하면 중복 체크가 O(1).  
또는 입력 단계에서 `set(report)`로 **전체 중복 제거** 후 처리.

---

### C. 최종 메일 카운트도 리스트 membership
```python
if j in send_li[i]:   # 여기서도 리스트 → O(len)
    answer[n] += 1
```
- `send_li[신고자]`를 set으로 바꾸면 `in`이 O(1)로 개선.

---

## 2) 권장 알고리즘 (정석)

1. **중복 신고 제거**: `unique = set(report)`  
2. 각 라인 `a b`에 대해:  
   - `reported_by[a].add(b)`  (신고자가 신고한 대상 set)  
   - `reported_count[b] += 1` (피신고자 신고 횟수)  
3. **정지 유저 집합**: `{u for u, c in reported_count.items() if c >= k}`  
4. **메일 수**: 각 유저 `a`에 대해 `reported_by[a]`와 `suspended`의 교집합 크기.

복잡도: O(|report| + |id_list| + 정렬 없음) — 평균 상수 해시.

---

## 3) 개선 코드

```python
def solution(id_list, report, k):
    # 1) 중복 신고 제거
    unique = set(report)

    # 2) 자료구조 준비
    reported_by = {u: set() for u in id_list}  # 신고자 -> (신고한 대상들)
    reported_cnt = {u: 0 for u in id_list}     # 피신고자 -> 신고당한 횟수

    # 3) 집계
    for rec in unique:
        a, b = rec.split()
        if b in reported_by[a]:
            continue
        reported_by[a].add(b)
        if b in reported_cnt:     # (안전) b가 id_list에 있는 경우만
            reported_cnt[b] += 1

    # 4) 정지 유저
    suspended = {u for u, c in reported_cnt.items() if c >= k}

    # 5) 메일 카운트 (id_list 순서대로)
    answer = []
    for u in id_list:
        cnt = sum(1 for target in reported_by[u] if target in suspended)
        answer.append(cnt)
    return answer
```

### 포인트
- 입력에서 **중복 신고**를 먼저 제거 (`set(report)`) → 이후 로직이 단순/안전.
- `reported_by[*]`를 **set**으로 관리하여 membership이 O(1).
- 최종 `suspended`도 **set**이므로 교집합 카운트 O(#신고한 대상).

---

## 4) 한 줄 요약
- **리스트 대신 set**으로 중복/멤버십 처리.
- **중복 신고는 입력 단계에서 제거**.
- **정지 유저는 set**으로 만들어 최종 카운트를 O(1) membership으로 계산.
- 이러면 시간 초과와 오답(중복 카운트) 모두 해결됩니다.
