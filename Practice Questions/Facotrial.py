def Factorial(num):
    result = 1
    for i in range(1,num + 1):
        result *= i
    return result

num = int(input("Enter a number:"))
if num < 0:
    print("Number can not be negative.")
else:
    print(f"{num}! = ",Factorial(num))