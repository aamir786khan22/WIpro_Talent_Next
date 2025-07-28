# Q1. Write a function to return the sum of all numbers in a list.
# Sample List : (8, 2, 3, 0, 7) | Expected Output : 20

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Q2. Write a function to return the reverse of a string.
# Sample String : "1234abcd" | Expected Output : "dcba4321"

def reverse_string(text):
    return text[::-1]

# Q3. Write a function to calculate and return the factorial of a number (a non-negative integer).

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Q4. Write a function that accepts a string and prints the number of upper case letters and lower case letters in it.

def count_case_letters(s):
    upper = 0
    lower = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    print("Upper case letters:", upper)
    print("Lower case letters:", lower)

# Q5. Write a function to print the even numbers from a given list. List is passed to the function as an argument.
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9] | Expected Result : [2, 4, 6, 8]

def even_numbers_from_list(nums):
    result = []
    for i in nums:
        if i % 2 == 0:
            result.append(i)
    return result

# Q6. Write a function that takes a number as a parameter and checks whether the number is prime or not.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Sample function calls for testing

# Q1 Test
print("Q1 Output:", sum_list([8, 2, 3, 0, 7]))  # Output: 20

# Q2 Test
print("Q2 Output:", reverse_string("1234abcd"))  # Output: dcba4321

# Q3 Test
print("Q3 Output:", factorial(5))  # Output: 120

# Q4 Test
count_case_letters("Hello World")  # Output: Upper case: 2, Lower case: 8

# Q5 Test
print("Q5 Output:", even_numbers_from_list([1, 2, 3, 4, 5, 6, 7, 8, 9]))  # Output: [2, 4, 6, 8]

# Q6 Test
print("Q6 Output (Is 17 prime?):", is_prime(17))  # Output: True
