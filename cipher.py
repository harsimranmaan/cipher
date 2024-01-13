message = input("Enter your message: ")
key = input("Enter your key: ")
operation = input("operation, type D/d for decryption ")
key = int(key) % 26
if operation == "D" or operation == "d":
    key = key * -1
lower_a_val= ord('a')
upper_a_val = ord('A')

letters =  list()
for char in message:
    int_val = ord(char)
    new_char = int_val
    if int_val >= lower_a_val and int_val < lower_a_val+26:
        new_char = ord(char) + int(key)
        if new_char > lower_a_val+26:
            new_char = new_char - 26
    if int_val >= upper_a_val and int_val < upper_a_val+26:
        new_char = ord(char) + int(key)
        if new_char > upper_a_val + 26:
            new_char =  new_char - 26
    letters.append(chr(new_char))

phrase = ''.join(letters)
print(message, key , phrase)