import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
all_characters = [letters, numbers, symbols]

while True:
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    if nr_letters == 0 and nr_symbols == 0 and nr_numbers == 0:
        print("⚠️ You must choose at least one character type. Please try again.\n")
    else:
        break


password = ""
password_length = nr_letters + nr_symbols + nr_numbers

for i in range(password_length):
    char_type = random.choice(all_characters)
    if char_type == letters and nr_letters > 0:
        password += random.choice(letters)
        nr_letters -= 1
    elif char_type == numbers and nr_numbers > 0:
        password += random.choice(numbers)
        nr_numbers -= 1
    elif char_type == symbols and nr_symbols > 0:
        password += random.choice(symbols)
        nr_symbols -= 1
    else:
        while True:
            if nr_letters > 0:
                password += random.choice(letters)
                nr_letters -= 1
                break
            elif nr_numbers > 0:
                password += random.choice(numbers)
                nr_numbers -= 1
                break
            elif nr_symbols > 0:
                password += random.choice(symbols)
                nr_symbols -= 1
                break
print(f"Your password is: {password}")

