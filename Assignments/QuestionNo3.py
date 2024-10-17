#Write a program that accepts two numbers and check if the first number is fully divisible by the second number or not.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num2 != 0:
    if num1 % num2 == 0:
        print(f"{num1} is fully divisible by {num2}.")
    else:
        print(f"{num1} is not fully divisible by {num2}.")
else:
    print("Division by zero is not allowed.")
