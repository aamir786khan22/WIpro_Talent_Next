'''
LIST QUESTIONS
'''

# 1. Write a program to create a list of 5 integers and display the list items. Access individual elements through index.
def show_list_elements():
    numbers = [10, 20, 30, 40, 50]
    print("Full List:", numbers)
    for idx in range(len(numbers)):
        print(f"Element at index {idx} is {numbers[idx]}")

# 2. Write a program to append a new item to the end of the list.
def add_item_to_end():
    items = [1, 2, 3, 4, 5]
    items.append(6)
    print("After appending:", items)

# 3. Write a program to reverse the order of the items in the list.
def reverse_items():
    nums = [10, 20, 30, 40, 50]
    nums.reverse()
    print("Reversed List:", nums)

# 4. Write a program to print the number of occurrences of a specified element in a list.
def count_element():
    data = [1, 2, 2, 3, 2, 4, 5]
    target = 2
    total = data.count(target)
    print(f"Occurrences of {target}: {total}")

# 5. Write a program to append the items of list1 to list2 in the front.
def combine_lists_front():
    a = [4, 5, 6]
    b = [1, 2, 3]
    combined = a + b
    print("Front appended list:", combined)

# 6. Write a program to insert a new item before the second element in an existing list.
def insert_before_index():
    items = [10, 20, 30, 40]
    items.insert(1, 15)
    print("Updated List:", items)

# 7. Write a program to remove the item from a specified index in a list.
def remove_at_position():
    elements = [10, 20, 30, 40, 50]
    pos = 2
    elements.pop(pos)
    print("List after removal:", elements)

# 8. Write a program to remove the first occurrence of a specified element from a list.
def remove_first_match():
    values = [1, 2, 3, 2, 4, 2]
    target = 2
    if target in values:
        values.remove(target)
        print("List after removing first occurrence:", values)
    else:
        print(f"{target} not found.")

