# import collections
from collections import OrderedDict

def solution(cacheSize, cities):
    # 캐시 미사용 특수 케이스
    if cacheSize == 0:
        return 5 * len(cities)

    cache = OrderedDict()
    time = 0

    for c in cities:
        city = c.lower()
        if city in cache:
            # hit: +1, 최근으로 이동
            time += 1
            cache.move_to_end(city, last=True)
        else:
            # miss: +5, 필요 시 LRU 하나 제거 후 추가
            time += 5
            if len(cache) == cacheSize:
                cache.popitem(last=False)  # 가장 오래된 항목 제거
            cache[city] = True

    return time

# not import collections
def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5 * len(cities)

    cache = []
    time = 0

    for city in cities:
        city = city.lower()
        if city in cache:
            # hit
            time += 1
            cache.remove(city)
            cache.append(city)
        else:
            # miss
            time += 5
            if len(cache) == cacheSize:
                cache.pop(0)  # 가장 오래된 도시 제거
            cache.append(city)

    return time

