with open("books/frankenstein.txt") as f:
    file_contents = f.read()
#Print Contents to console
#     print(file_contents)
# Count number of words in the text
words = len(file_contents.split())
print (f"Text has {words} words")
#Count occurance of any letter in the book. Convert to lowercase
lower_contents = file_contents.lower()
print("Counts the occurrence of each letter in the text")
letters = "a"
while letters != "{":
    print(f"{letters} = {lower_contents.count(letters)}")
# Increment letter by 1
    letters = (chr(ord(letters)+1)) 