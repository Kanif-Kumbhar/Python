#WAP to display frequencies of all the elements of a list.

def display_frequencies(lst):
    frequency_dict = {}
    for item in lst:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    return frequency_dict

user_input = input("Enter numbers separated by spaces: ")
user_list = list(map(int, user_input.split()))

frequencies = display_frequencies(user_list)

for key, value in frequencies.items():
    print(f"Element {key} occurs {value} times")