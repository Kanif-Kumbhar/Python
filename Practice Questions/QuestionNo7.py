# Write a program to print a pattern like:
# 4   3   2   1
# 4   3   2
# 4   3
# 4 

def print_pattern(n):
    for i in range(n, 0, -1):
        for j in range(n, n-i, -1):
            print(j, end="   ")
        print()

n = 4
print_pattern(n)
