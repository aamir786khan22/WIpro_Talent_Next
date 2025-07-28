'''
TUPLE QUESTIONS
'''

# 1. Write a program to print the 4th element from first and 4th element from last in a tuple.
def fourth_elements():
    items = (5, 10, 15, 20, 25, 30, 35, 40)
    print("4th from start:", items[3])
    print("4th from end:", items[-4])

# 2. Write a program to check whether an element exists in a tuple or not.
def is_present_in_tuple():
    fruits = ('apple', 'banana', 'cherry')
    search = 'banana'
    if search in fruits:
        print(f"{search} exists")
    else:
        print(f"{search} does not exist")

# 3. Write a program to convert a list into a tuple.
def convert_list_to_tuple():
    data = [1, 2, 3, 4, 5]
    result = tuple(data)
    print("Converted tuple:", result)

# 4. Write a program to find the index of an item in a tuple.
def index_of_item():
    tup = ('a', 'b', 'c', 'd', 'e')
    target = 'c'
    if target in tup:
        print(f"Index of {target}: {tup.index(target)}")

# 5. Write a program to replace last value of tuples in a list to 100.  
def update_tuple_list():
    data = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
    changed = [t[:-1] + (100,) for t in data]
    print("Modified tuples:", changed)
