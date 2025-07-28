

'''
STRING QUESTIONS
'''

# 1. Write a program to count the number of upper and lower case letters in a String.
def count_case_letters():
    msg = "Hello World"
    upper = 0
    lower = 0
    for char in msg:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    print("Uppercase:", upper)
    print("Lowercase:", lower)

# 2. Write a program that will check whether a given String is Palindrome or not.
def is_string_palindrome():
    txt = "madam"
    reversed_txt = txt[::-1]
    if txt == reversed_txt:
        print(f"{txt} is a palindrome")
    else:
        print(f"{txt} is not a palindrome")

# 3. Given a string, return a new string made of n copies of the first 2 chars of the original string where n is the length of the string.
# If input is "Wipro" then output should be "WiWiWiWiWi".
def repeat_start_chars():
    text = "Wipro"
    length = len(text)
    part = text[:2]
    result = ""
    for _ in range(length):
        result += part
    print("New String:", result)

# 4. Given a string, if the first or last character is 'x', return the string without those 'x' character, else return the string unchanged.
# If the input is "xHix", then output is "Hi".
def remove_x_edges():
    value = "xHix"
    if len(value) > 0 and value[0] == 'x':
        value = value[1:]
    if len(value) > 0 and value[-1] == 'x':
        value = value[:-1]
    print("Cleaned string:", value)

# 5. Given a string and an integer n, return a string made of n repetitions of the last n characters of the string.
# For example if the inputs are “Wipro” and 3, then the output should be “propropro”.
def repeat_last_chars():
    text = "Wipro"
    n = 3
    end_part = text[-n:]
    result = ""
    for _ in range(n):
        result += end_part
    print("Repeated string:", result)
