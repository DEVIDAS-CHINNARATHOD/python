# Simple program to remove duplicate words from a list

words = ["apple", "banana", "apple", "cherry", "banana", "mango"]
print("Original list:", words)

unique_words = []  # Empty list to store unique words

for word in words:
    if word not in unique_words:
        unique_words.append(word)

print("List after removing duplicates:", unique_words)

