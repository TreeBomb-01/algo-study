n = int(input())
six=665
count=0
while True:
    six+=1
    if "666" in str(six):
        count+=1
        if count==n:
            print(six)
            break