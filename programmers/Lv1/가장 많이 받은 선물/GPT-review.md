# 코드 리뷰: 선물 예측 문제 (Python)

## 요약
- 현재 코드는 `(i, j)`와 `(j, i)`를 **모두 평가**한 뒤 `max(gift) / 2`로 보정해 정답을 맞추는 방식입니다.  
- 동작은 가능하나, **비효율적(O(n³))이며, 취약**하고, 불필요하게 복잡합니다.  
- 각 쌍을 **한 번(i < j)**만 평가하고, **선물 지수(준-받은)**를 **사전에 계산**하는 방식이 더 안전하고 빠릅니다.  

---

## 문제점 상세

### 1) 한 쌍을 두 번 세는 구조
```python
for i in range(len(gift_c)):
    for j in range(len(gift_c)):
        if i != j:
            ...
```
- `(i, j)`와 `(j, i)`를 둘 다 처리하여 승자에게 **2번 가산**되는 구조입니다.  
- 마지막에 `return max(gift)/2`로 보정하지만, 이는 **핵(hack)**에 가깝고 유지보수에 취약합니다.  

✅ **권장**: `for j in range(i+1, n)`로 쌍을 한 번만 평가하세요.  

---

### 2) 선물 지수 계산의 반복 (불필요한 O(n³))
```python
elif gift_c[i][j] == gift_c[j][i]:
    i_g = i_t = j_g = j_t = 0
    for k in range(len(gift_c)):
        i_g += gift_c[k][i]      # i가 받은 합
        i_t += gift_c[i][k]      # i가 준 합
        j_g += gift_c[k][j]
        j_t += gift_c[j][k]
```
- 매 동률 케이스마다 **row/column 합산을 재계산**합니다.  

✅ **권장**: gifts 집계 후  
- `sent[i]` = i가 준 총합  
- `recv[i]` = i가 받은 총합  
을 한 번만 계산하고,  
`gift_index[i] = sent[i] - recv[i]`로 저장하여 비교 시 O(1)로 사용하세요.  

---

### 3) 이름 인덱스 탐색의 선형 비용
```python
send = name.index(p[0])
take = name.index(p[1])
```
- `gifts` 길이가 최대 10,000이고, `index()`가 O(n)이라 숨은 비용이 큽니다.  

✅ **권장**:
```python
idx = {name: i for i, name in enumerate(friends)}
```
이렇게 딕셔너리를 만들어 O(1) 조회.  

---

### 4) 내장 함수 이름 가리기
```python
max = 0
...
return max(gift)/2
```
- 파이썬 내장 `max()`를 가리면 디버깅/협업에서 문제를 일으킬 수 있습니다.  

✅ **권장**: `best = 0` 같은 다른 변수명을 사용하세요.  

---

### 5) 반환 타입 (정수)
```python
return max(gift)/2
```
- `/`는 **float**를 반환합니다. 문제는 정수 반환을 기대합니다.  

✅ **권장**: `// 2` 또는 `int()`로 보정하세요.  
더 나은 방법은 **애초에 쌍을 한 번만 세어 보정이 필요 없게 만드는 것**입니다.
