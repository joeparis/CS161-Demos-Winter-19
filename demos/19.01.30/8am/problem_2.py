user_input = input("Please enter a string: ")

# for character in user_input:
#     print(f"{character} = {ord(character):3}")

# k = []
# for a in user_input:
#     k.append(ord(a))

k = [ord(a) for a in user_input]

print(k)
