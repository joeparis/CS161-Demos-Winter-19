#!/usr/bin/evn python3
import string

# simple_reader = open("simple_text.txt")
# # work with the file
# simple_reader.close()

with open("simple_text.txt", "r", encoding="utf-8") as simple_reader:
    translator = str.maketrans("", "", string.punctuation)
    sb_list = simple_reader.read().translate(translator).split()
    sb_list.sort(key=str.lower)

    average_len = sum(len(word) for word in sb_list) / len(sb_list)

    print(sb_list)
    print(f"{average_len:.1f}")
