user_input = input("Please enter a string: ")

# find out what the first character is
# replace all instances of that character EXCEPT the first one with '$'

# new_string = user_input[0] + user_input[1:].replace(user_input[0], "$")

first_character = user_input[0]
rest_of_string = user_input[1:]
rest_of_string.replace(first_character, "$")
new_string = first_character + rest_of_string


print(user_input)
print(new_string)
