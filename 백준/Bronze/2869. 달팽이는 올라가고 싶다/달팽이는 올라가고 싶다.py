a, b, v = map(int, input().split())
day = (v - a + (a - b) - 1) // (a - b) + 1
print(day)
