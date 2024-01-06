message = input("Enter your message: ")
key = input("Enter your key: ")

for char in message:
    new_char = ord(char) + int(key)
    print(char, ord(char), new_char)

print(message, key)