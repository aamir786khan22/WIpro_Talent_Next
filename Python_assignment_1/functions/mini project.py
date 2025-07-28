	# Sort the colors	Functions
def sort_colors(data):
    colors = data.split("-")
    colors.sort()
    return "-".join(colors)

input1 = "green-red-yellow-black-white"
print(sort_colors(input1))

input2 = "PINK-BLUE-TAN-PURPLE"
print(sort_colors(input2))

# Playing with names	Modules
# module.py
def ispalindrome(name):
    name = name.replace(" ", "")
    if name == name[::-1]:
        print("Yes it is a palindrome.")
    else:
        print("No it is not a palindrome.")

def count_the_vowels(name):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in name:
        if ch in vowels:
            count += 1
    print("No of vowels:", count)

def frequency_of_letters(name):
    name = name.replace(" ", "")
    freq = {}
    for ch in name:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    for ch in sorted(freq.keys()):
        print(f"{ch}-{freq[ch]}", end=", ")

# main.py
import mymodule

name1 = "bob"
mymodule.ispalindrome(name1)
mymodule.count_the_vowels(name1)
mymodule.frequency_of_letters(name1)

print()

name2 = "marcelbentok tanaka"
mymodule.ispalindrome(name2)
mymodule.count_the_vowels(name2)
mymodule.frequency_of_letters(name2)
