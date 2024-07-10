text = input("Enter a sentence for tokenization: ")
str = []
current_str = ""

for char in text:
    if char != ' ':
        current_str += char
    else:
        str.append(current_str)
        current_str = ""

if current_str:
    str.append(current_str)

for str in str:
    print(str)