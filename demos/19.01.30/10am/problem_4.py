# coding=utf-8

user_input = input("Please enter a string: ")

# first_character = user_input[0]
# rest_of_string = user_input[1:]
# string_with_replacement = rest_of_string.replace(first_character, "$")
# new_string = first_character + string_with_replacement

new_string = user_input[0] + user_input[1:].replace(user_input[0], "$")

print(user_input)
print(new_string)
