


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

def caesar_decrypt(encrypted_string, key):
	"""Complete TASK 2 here!"""
	decrypted_string = ""
	lower_case = "abcdefghijklmnopqrstuvwxyz"
	upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for letter in encrypted_string:
		if letter in lower_case:
			new_letter_index = lower_case.index(letter) - key
			if new_letter_index > 26:
				new_letter_index -= 26
			decrypted_string = decrypted_string + lower_case[new_letter_index]
		elif letter in upper_case:
			new_letter_index = upper_case.index(letter) - key
			if new_letter_index > 26:
				new_letter_index -= 26
			decrypted_string = decrypted_string + upper_case[new_letter_index]
		else:
			pass
	return decrypted_string


# Complete TASK 3 - creating your own cipher function - here!
def my_cipher(input_string, mode):
	plain_text = "abcdefghijklmnopqrstuvwxyz"
	cipher_text = "tQp.jVR2-9B3Diwg2hl0WzvPUZ"
	if mode == "encrypt":
		final_string = ""
		for i in input_string:
			character_index = plain_text.index(i) 
			final_string = final_string + cipher_text[character_index]
	elif mode == "decrypt":
		final_string = ""
		for i in input_string:
			character_index = cipher_text.index(i) 
			final_string = final_string + plain_text[character_index]
	return final_string

