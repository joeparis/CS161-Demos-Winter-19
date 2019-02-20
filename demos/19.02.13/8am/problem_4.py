#! /usr/bin/env python3

words = input("Please enter a comma separated list of words:")

# Levi's
list = [x.strip() for x in (",")]
list_2 = set(list)
list_3 = sorted(list_2)
list = sorted(set([x.strip() for x in (",")]))
print(list_3)

# Georgi's
# words_2 = words.replace(" ", "")
# words_3 = words_2.split(",")
# words_4 = sorted(words_3)

# unique_words = []
# for word in words_4:
#     if word not in unique_words:
#         unique_words.append(word)

# print(words_4)
# print(unique_words)
