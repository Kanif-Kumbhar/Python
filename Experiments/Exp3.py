num_terms = int(input("\nEnter the number of terms in the Fibonacci series: "))

a, b = 0, 1
count = 0

print("Fibonacci Series:")
while count < num_terms:
    print(a, end=" ")

    a, b = b, a + b
    count += 1