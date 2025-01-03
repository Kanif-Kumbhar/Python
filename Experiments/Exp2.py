age = int(input("\nEnter your age >> "))

if age < 10:
    print("You're a child")
elif 10 <= age < 18:
    print("You're a teenager")
elif 18 <= age < 60:
    print("You're an adult")
else:
    print("You're a senior citizen")
