string_1 = input("Please enter the first string: ")
string_2 = input("Please enter the second string: ")

# string_1_first_char = string_1[0]
# string_2_first_char = string_2[0]

# new_1 = string_2_first_char + string_1[1:]
# new_2 = string_1_first_char + string_2[1:]


new_1, new_2 = string_2[0] + string_1[1:], string_1[0] + string_2[1:]

print(string_1, string_2)
print(new_1, new_2)
