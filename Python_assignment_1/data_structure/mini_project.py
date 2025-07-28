
#People and facts -	Dictionary
people = {
    "Jeff": "Is afraid of Dogs.",
    "David": "Plays the piano.",
    "Jason": "Can fly an airplane."
}

for name, fact in people.items():
    print(name + ": " + fact)

people["Jeff"] = "Is afraid of heights."
people["Jill"] = "Can hula dance."

print()

for name, fact in people.items():
    print(name + ": " + fact)

# Find the Runner-Up Score	List

scores = [2, 3, 6, 6, 5]
unique_scores = list(set(scores))
unique_scores.sort()
print(unique_scores[-2])


# 	Find the Percentage	Dictionary and List
records = {
    "Krishna": [67, 68, 69],
    "Arjun": [70, 98, 63],
    "Malika": [52, 56, 60]
}

name = input("Enter a name: ")
marks = records[name]
average = sum(marks) / len(marks)
print("Average percentage mark:", int(average))


# Find the name	String
text = "Hi Alex WelcomeAlex Bye Alex"
count = text.count("Alex")
print(count)
