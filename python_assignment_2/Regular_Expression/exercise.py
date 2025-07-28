import re
import requests

# 1. Check if a string has only octal digits
print("1. Check if string has only octal digits")
strings = ['789', '123', '004']
for s in strings:
    if re.fullmatch(r'[0-7]+', s):
        print(f"{s}: Valid Octal")
    else:
        print(f"{s}: Not Octal")

print("\n2. Extract user id, domain, and suffix from emails")
emails = """zuck@facebook.com
sunder33@google.com
jeff42@amazon.com"""

for email in emails.splitlines():
    match = re.match(r'(\w+)@(\w+)\.(\w+)', email)
    if match:
        print(match.groups())

print("\n3. Split irregular sentence into words")
sentence = "A, very   very; irregular_sentence"
words = re.split(r'[;,_\s]+', sentence)
print(" ".join(words))

print("\n4. Clean tweet")
tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''
cleaned = re.sub(r'RT|cc:|http\S+|@\S+|#\S+|[^\w\s]', '', tweet)
print(" ".join(cleaned.split()))

print("\n5. Extract text from HTML tags")
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
text = r.text
matches = re.findall(r'>([^<]+)<', text)
cleaned_matches = [m.strip() for m in matches if m.strip()]
print(cleaned_matches)

print("\n6. Words that begin and end with the same character")
words = ['civic', 'trust', 'widows', 'maximum', 'museums', 'aa', 'as']
for word in words:
    if len(word) >= 1 and word[0] == word[-1]:
        print(word)
