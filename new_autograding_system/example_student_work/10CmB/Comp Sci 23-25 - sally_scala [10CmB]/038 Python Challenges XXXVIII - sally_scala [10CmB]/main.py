def rot13_encrypt(text):
	"""Complete TASK 1 here!"""
	final = ""
	for i in text:
		number = ord(i)
		i = number + 13
		if i > 122:
			i = i - 26
		letter = chr(i)
		final = final + letter
	return final


def caesar_decrypt(text, shift):
	"""Complete TASK 2 here!"""
	for i in text:
		number = ord(i)
		i = number + shift
		if i > 122:
			i = i - 26
		elif i > 90 and i < 97:
			i = i - 26
		letter = chr(i)
		print(letter, end="")




# Complete TASK 3 - creating your own cipher function - here!




assert rot13_encrypt("cat") == "png"


