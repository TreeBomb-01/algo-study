def solution(cacheSize, cities):
    cities_l = [i.lower() for i in cities]
    answer = 0
    cache=set()
    for i in range(len(cities_l)):
        if cities_l[i] in cache:
            answer+=1
        else:
            answer+=5
            if len(cache) < cacheSize:
                cache.add(cities_l[i])
            else:
                cache.clear()
                j=0
                while len(cache) != cacheSize:
                    cache.add(cities_l[i-j])
                    j+=1

    return answer