def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num - 1) 

number = int(input("Enter number: "))
if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")
