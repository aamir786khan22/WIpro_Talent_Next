'''
DICTIONARY QUESTIONS
'''

# 1. Write a program to add a key and value to a dictionary.   
def insert_key_value():
    student = {0: 10, 1: 20}
    student[2] = 30
    print("Dictionary after adding:", student)

# 2. Write a program to concatenate the following dictionaries to create a new one.  
def merge_dicts():
    d1 = {1: 10, 2: 20}
    d2 = {3: 30, 4: 40}
    d3 = {5: 50, 6: 60}
    final = {}
    for each in (d1, d2, d3):
        final.update(each)
    print("Merged dictionary:", final)

# 3. Write a program to check if a given key already exists in a dictionary.
def key_presence_check():
    info = {1: "apple", 2: "banana", 3: "cherry"}
    check = 2
    if check in info:
        print(f"Key {check} exists.")
    else:
        print(f"Key {check} does not exist.")

# 4. Write a program to iterate over a dictionary using for loop and print the keys alone, values alone and both keys and values.
def loop_dict_elements():
    data = {'a': 1, 'b': 2, 'c': 3}
    print("Keys:")
    for k in data:
        print(k)
    print("Values:")
    for v in data.values():
        print(v)
    print("Key-Value Pairs:")
    for k, v in data.items():
        print(f"{k}: {v}")

# 5. Write a program to prepare a dictionary where the keys are numbers between 1 and 15 and the values are squares of the keys.
def square_key_dict():
    squares = {num: num ** 2 for num in range(1, 16)}
    print("Squares Dictionary:", squares)

# 6. Write a program to sum all the values in a dictionary, considering the values will be of int type.
def total_dict_values():
    amounts = {'a': 100, 'b': 200, 'c': 300}
    result = sum(amounts.values())
    print("Total sum:", result)