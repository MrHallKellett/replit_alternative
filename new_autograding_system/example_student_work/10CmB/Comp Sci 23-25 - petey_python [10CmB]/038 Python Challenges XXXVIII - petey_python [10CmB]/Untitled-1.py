
def rot13_encrypt(user_string):
	"""Complete TASK 1 here!"""
	encrypted_string = ""
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for letter in user_string:
		new_letter_index = alphabet.index(letter) + 13
		if new_letter_index > 26:
			new_letter_index -= 26
		encrypted_string = encrypted_string + alphabet[new_letter_index]
	return encrypted_string

print(rot13_encrypt("cat"))

def caesar_decrypt(encrypted_string, key):
	"""Complete TASK 2 here!"""
	decrypted_string = ""
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	for letter in encrypted_string:
		if letter in alphabet:
			new_letter_index = alphabet.index(letter) - key
			if new_letter_index > 26:
				new_letter_index -= 26
			decrypted_string = decrypted_string + alphabet[new_letter_index]
		else:
			pass
	return decrypted_string

print(caesar_decrypt("zhbzhnlz", 7))