# 1. Write a program to read the entire content from a txt file and display it to the user.
def read_entire_file():
    with open("sample.txt", "r") as file:
        content = file.read()
        print("\n--- Full File Content ---")
        print(content)

# 2. Write a program to read first n lines from a txt file. Get n as user input.
def read_first_n_lines():
    n = int(input("Enter number of lines to read: "))
    with open("sample.txt", "r") as file:
        print(f"\n--- First {n} Lines ---")
        for i in range(n):
            line = file.readline()
            if line:
                print(line.strip())
            else:
                break

# 3. Write a program to accept input from user and append it to a txt file.
def append_to_file():
    text = input("Enter text to append to the file: ")
    with open("sample.txt", "a") as file:
        file.write(text + "\n")
    

# 4. Write a program to read contents from a txt file line by line and store each line into a list.
def read_lines_to_list():
    with open("sample.txt", "r") as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    print("\n--- Lines Stored in List ---")
    print(lines)

# 5. Write a program to find the longest word from the txt file contents, assuming that the file will have only one longest word in it.
def find_longest_word():
    with open("sample.txt", "r") as file:
        words = file.read().split()
    longest = max(words, key=len)
    print("\nLongest word in the file is:", longest)

# 6. Write a program to count the frequency of a user entered word in a txt file.
def count_word_frequency():
    word = input("Enter the word to count its frequency: ")
    with open("sample.txt", "r") as file:
        words = file.read().split()
    count = words.count(word)
    print(f"The word '{word}' appears {count} times in the file.")



