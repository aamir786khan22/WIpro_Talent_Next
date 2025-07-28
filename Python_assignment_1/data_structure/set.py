'''
SET QUESTIONS
'''

# 1. Write a program to remove a given item from the set.
def delete_item_from_set():
    numbers = {1, 2, 3, 4, 5}
    to_remove = 3
    if to_remove in numbers:
        numbers.remove(to_remove)
    print("Updated set:", numbers)

# 2. Write a program to create an intersection of sets.
def set_intersection_manual():
    first = {1, 2, 3, 4}
    second = {3, 4, 5, 6}
    result = set()
    for item in first:
        if item in second:
            result.add(item)
    print("Common values:", result)

# 3. Write a program to create a union of sets.
def set_union_manual():
    a = {1, 2, 3}
    b = {3, 4, 5}
    result = set()
    for x in a:
        result.add(x)
    for x in b:
        result.add(x)
    print("Combined set:", result)

# 4. Write a program to find the maximum and minimum value in a set.
def find_max_min():
    items = {10, 20, 5, 30}
    max_val = None
    min_val = None
    for val in items:
        if max_val is None or val > max_val:
            max_val = val
        if min_val is None or val < min_val:
            min_val = val
    print("Max:", max_val)
    print("Min:", min_val)