#WAP to display the second largest element of a given list.

def second_largest(lst):
    unique_lst = list(set(lst))
    unique_lst.sort()
    return unique_lst[-2]

user_input = input("Enter numbers separated by spaces: ")
user_list = list(map(int, user_input.split()))

print("The second largest element is:", second_largest(user_list))