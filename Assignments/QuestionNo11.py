#WAP in Python to find and display the sum of all the values which are ending with 3 from  a list.

def sum_of_values_ending_with_3(lst):
    return sum(num for num in lst if str(num).endswith('3'))

user_input = input("Enter numbers separated by spaces: ")
user_list = list(map(int, user_input.split()))

result = sum_of_values_ending_with_3(user_list)

print("The sum of all values ending with 3 is:", result)