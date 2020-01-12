letters = "abcdefghijklmnopqrstuvwxyz"
letters_upper= letters.upper()
numbers = "0123456789"
special = "!@#$%^&*()-_+=/?|"



def check_letters(password):
	for char in password:
		if char in letters:
			return True
	print("Password-i nuk permban shkronja te vogla !")
	return False

def check_letters_upper(password):
	for char in password:
		if char in letters_upper:
			return True
	print("Password-i nuk permban shkronja te medha !")
	return False

def check_numbers(password):
	for char in password:
		if char in numbers:
			return True
	print("Password-i nuk permban numra !")
	return False

def check_special(password):
	for char in password:
		if char in special:
			return True
	print("Password-i nuk permban karaktere te vecanta !")
	return False

valid_passwords = []
n = input("Passwords:")
list_of_passwords = n.split(",")
for element in list_of_passwords:
	if 6 <= len(element) <= 12:
		if check_special(element) and check_numbers(element) and check_letters(element) and check_letters_upper(element):
			valid_passwords.append(element)

print("Valid Passwords: ", valid_passwords)