#Write a python script to print the following pattern.
# 1
# 1    3
# 1    3     5
# 1    3     5     7

n = 4 

for i in range(1, n + 1):
    num = 1
    for j in range(i):
        print(num, end="    ")
        num += 2
    print()