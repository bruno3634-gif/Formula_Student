n = input()
n = int(n)

for x in range(n+1):
    if x%2 == 0:
        if x == 0:
            print("FizzBuzz")
        elif x== 14:
            print("Fizz")

    elif x == 7:    
        print("Buzz")
    # else:
       # print(x)   
    else:
        print(x)
