def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

string = input("\nEnter a string: ")

if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
