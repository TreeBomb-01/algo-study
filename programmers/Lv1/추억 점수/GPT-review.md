# GPT-review: 추억 점수(사진 속 인물 합산) — 세 가지 풀이 비교 리뷰

## ✅ 개요
- 목표: `name`과 `yearning`으로 사람→점수 매핑을 만든 뒤, 각 `photo`(이름 목록)의 점수를 합산하여 리스트로 반환.
- 세 풀이 모두 **정답은 동일**합니다. 핵심 차이는 **시간 복잡도와 가독성**입니다.

---

## 1) 당신의 풀이

```python
def solution(name, yearning, photo):
    answer = []
    p = {i: j for i, j in zip(name, yearning)}
    for i in photo:
        score = 0
        for j in i:
            if j in p:
                score += p[j]
        answer.append(score)
    return answer
```

### 장점
- 딕셔너리를 한 번 구성하여 **O(1) 조회**로 합산 → 효율적.
- 절차가 명확해 **가독성** 좋음.
- 제약(중복 없음) 하에서 **정확성/성능 밸런스** 우수.

### 개선 여지
- 파이썬다운 축약(컴프리헨션, `get`)을 쓰면 조금 더 간결해질 수 있음(아래 2번).

---

## 2) 제안 풀이(파이썬스러운 축약)

```python
def solution(name, yearning, photo):
    score_map = dict(zip(name, yearning))
    return [sum(score_map.get(person, 0) for person in people) for people in photo]
```

### 특징
- 한 줄 컴프리헨션으로 **간결 + 성능 동일**.
- `dict.get(k, 0)`으로 **미등록 이름 0 처리**를 자연스럽게 표현.
- 실전에서 가장 추천되는 형태.

---

## 3) 다른 사람 풀이(리뷰 대상)

```python
def solution(이름, 점수, 사진):
    return [sum(점수[이름.index(j)] for j in i if j in 이름) for i in 사진]
```

### 동작 방식
- `이름.index(j)`로 매번 인덱스를 찾아 그 인덱스로 `점수[...]`에 접근하여 합산.

### 문제점(성능)
- `list.index`는 **O(n)** 선형 탐색입니다.
- 전체 복잡도는 대략 **O(사진_개수 × 사진_당_인물수 × 이름_수)** 입니다.
  - 최악(각 100) 가정 시: 100 × 100 × 100 = **1,000,000번 탐색** 수준(상수 제외) → 입력이 커질수록 **느려질 수 있음**.
- 반면, 딕셔너리 조회는 **평균 O(1)** → 위와 동일 조건에서 **수십 배 이상 빠를 수 있음**.

### 기타
- `if j in 이름` 또한 리스트 membership → **O(n)**가 추가로 들어감.
- 동작은 맞지만, **리스트 기반 회원 조회 + index 반복**은 파이썬에서 권장되지 않는 패턴.

### 개선 방향
- 한 줄 형태를 유지하고 싶다면, 최소한 **딕셔너리로 사전 매핑**을 만들고 접근해야 합니다.

```python
def solution(name, yearning, photo):
    score_map = dict(zip(name, yearning))
    return [sum(score_map.get(person, 0) for person in people) for people in photo]
```

---

## 성능 비교 요약

| 풀이 | 조회 방식 | 시간 복잡도(대략) | 가독성 | 비고 |
|---|---|---|---|---|
| 당신의 풀이 | dict 조회 O(1) | O(총_이름_합계) | 좋음 | 실전에서 충분히 최적 |
| 제안 풀이 | dict 조회 O(1) | O(총_이름_합계) | 아주 좋음 | 가장 추천 |
| 다른 사람 풀이 | list.index O(n) + `in` O(n) | O(사진×사진원소×이름) | 보통 | 입력 커지면 느려짐 |

> ✅ 결론: **딕셔너리 매핑 후 합산**이 가장 바람직합니다.  
> 다른 사람 풀이도 정답이지만, **리스트에서 매번 index/in을 쓰는 방식은 비효율**입니다.

---

## 최종 추천 코드

```python
def solution(name, yearning, photo):
    score_map = dict(zip(name, yearning))
    return [sum(score_map.get(person, 0) for person in people) for people in photo]
```
