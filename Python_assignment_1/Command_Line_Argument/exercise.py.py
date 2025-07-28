import sys

# Program to accept two numbers as command line arguments and display their sum
# Check if two arguments are given (excluding script name)
if len(sys.argv) != 3:
    print("Please provide exactly two numbers.")
else:
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])
    total = num1 + num2
    print("Sum:", total)


# Program to accept a welcome message and display the file name with it
file_name = sys.argv[0]
msg = " ".join(sys.argv[1:])

if msg:
    print("File Name:", file_name)
    print("Welcome Message:", msg)
else:
    print("Please enter a welcome message.")



# Program to accept 10 numbers and calculate the sum of prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

args = sys.argv[1:]

if len(args) != 10:
    print("Please enter exactly 10 numbers.")
else:
    numbers = [int(x) for x in args]
    prime_sum = sum(num for num in numbers if is_prime(num))
    print("Sum of prime numbers:", prime_sum)
