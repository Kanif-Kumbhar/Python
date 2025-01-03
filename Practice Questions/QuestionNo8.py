#WAP to remove all odd numbers from the given list.

def remove_odd_numbers(lst):
    return [num for num in lst if num % 2 == 0]

user_input = input("Enter numbers separated by spaces: ")
user_list = list(map(int, user_input.split()))

filtered_list = remove_odd_numbers(user_list)

print("List after removing odd numbers:", filtered_list)