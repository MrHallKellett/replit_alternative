


def rot13_encrypt(string):
	"""Complete TASK 1 here!"""
	text = ""
	for char in string: 
		ascii_value = ord(char)
		if ascii_value >= 91: 
			x =	ascii_value + 13
		elif 65 < ascii_value < 77:
			x = ascii_value + 13
		elif 78 < ascii_value < 90:
			x = ascii_value - 13
		else: 
			print("Error")

		encrypted = chr(x)
		text += encrypted
		print(encrypted)
	
	return text
assert rot13_encrypt("hello") == "uryyb"
assert rot13_encrypt("cat") == "png"





def caesar_decrypt(encrypted_string, key):
	"""Complete TASK 2 here!"""
	letter = " "
	for letter in encrypted_string: 
		 ascii_value = ord(letter)
	if letter >= 91: 
			x =	letter+ 13
	elif 65 < letter < 77:
			x = letter + 13
	elif 78 < letter < 90:
			x = letter - 13
		else: 
			print("Error")
	key = 


# Complete TASK 3 - creating your own cipher function - here!

