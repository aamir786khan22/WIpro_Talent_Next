# 1. Division of two numbers with exception handling
def divide_numbers():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        result = a / b
        print("Result:", result)
    except Exception as e:
        print("Error:", e)

# 2. Check whether a number is prime with exception handling
def check_prime():
    try:
        num = int(input("Enter a number to check prime: "))
        if num < 2:
            print("Not a prime number.")
            return
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                print("Not a prime number.")
                return
        print("It is a prime number.")
    except ValueError:
        print("Error: Please enter a valid integer.")

# 3. Read file contents and print in title case
def read_file_title_case():
    try:
        filename = input("Enter file name: ")
        with open(filename, "r") as file:
            content = file.read()
            print("\n--- File Content in Title Case ---")
            print(content.title())
    except FileNotFoundError:
        print("Error: File does not exist.")
    except Exception as e:
        print("Error:", e)

# 4. Check if number at index is positive or negative
def check_number_in_list():
    numbers = [10, -5, 3, -2, 8, -9, 4, 7, -1, 6]
    try:
        index = int(input("Enter index (0-9): "))
        value = numbers[index]
        if value >= 0:
            print("The number at index", index, "is Positive.")
        else:
            print("The number at index", index, "is Negative.")
    except IndexError:
        print("Error: Invalid index.")
    except ValueError:
        print("Error: Please enter a valid integer.")


