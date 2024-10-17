#Write a program that reads the number n and prints the value of n², n³ and n⁴.

n = int(input("Enter a number: "))

n_squared = n ** 2
n_cubed = n ** 3
n_fourth = n ** 4

print(f"n² = {n_squared}")
print(f"n³ = {n_cubed}")
print(f"n⁴ = {n_fourth}")