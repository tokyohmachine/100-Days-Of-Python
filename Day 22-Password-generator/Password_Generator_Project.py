import random

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
letters = int(input("How many Letters_birth would you like in your password?\n"))
symbols = int(input(f"How many symbols would you like?\n"))
numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = &!JduE91

password = ''

for char in range(1, letters + 1):
    password += random.choice(LETTERS)

for char in range(1, numbers + 1):
    password += random.choice(NUMBERS)

for char in range(1, symbols + 1):
    password += random.choice(SYMBOLS)
# print(password)

# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = ^g2jk&8P
# hard_level

password1 = []

for char in range(1, letters + 1):
    password1.append(random.choice(LETTERS))

for char in range(1, numbers + 1):
    password1.append(random.choice(NUMBERS))

for char in range(1, symbols + 1):
    password1.append(random.choice(SYMBOLS))

random.shuffle(password1)

password = ''
for char in password1:
    password += char
print(password)

