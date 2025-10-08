def solution(name, yearning, photo):
    score_map = dict(zip(name, yearning))
    return [sum(score_map.get(person, 0) for person in people) for people in photo]