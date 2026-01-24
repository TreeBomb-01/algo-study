for i in range(3):
    a = input()
    if a.isdigit():
        num = int(a)+3-i
if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)