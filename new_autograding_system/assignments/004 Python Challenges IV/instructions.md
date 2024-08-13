# Python Challenges IV

## Indefinite iteration - WHILE

---

### Example
	
	## repeat until the user enters a word
	name = ""
	while name == "":	
	    name = input("What's your name? ")
	print("Thanks for telling me your name.")
	

---

### Credentials

1\. To access secret government files, the username is "TheresaMay123" and the password is "abcdef". Repeatedly ask the user to enter the credentials until they are welcomed into the system.
	
	Enter username:
	TonyBlair99
	Enter password:
	p4ssw0rd
	INCORRECT CREDENTIALS.
	Enter username:
	GordonBrown45
	Enter password:
	123456
	INCORRECT CREDENTIALS.
	Enter username:
	DavidCameron09
	Enter password:
	downingstreet
	INCORRECT CREDENTIALS.
	Enter username:
	TheresaMay123
	Enter password:
	abcdef
	CORRECT CREDENTIALS.
	Welcome to the system.
	

---

### **Enough**

2\. Write a program that repeatedly asks the user if they've "had enough". The user has "had enough" when this has a) happened 5 times or b) they have answered the question with the word "enough" (ignoring spaces and case).
	
	Have you had enough?	
	no	
	Have you had enough?	
	no	
	Have you had enough?	
	no	
	Have you had enough?	
	no	
	Have you had enough?	
	no	
	You've had enough.
	
	## another test run...
	
	Have you had enough?	
	no	
	Have you had enough?	
	yes	
	Have you had enough?	
	ENOUGH	
	You've had enough.
	
---
	
### Countdown

3\. Ask the user to enter a number. Repeatedly subtract this number from 100 - displaying the countdown as you go - until the number is no longer positive. To conclude, display the message "FINISHED".
	
	Enter number:	
	44
	100
	56
	12
	FINISHED
	
	## another test run...
	
	Enter number:	
	10
	100
	90
	80
	70
	60
	50
	40
	30
	20
	10
	FINISHED
	
---

### Confirmation Attempts

4\. Password confirmation is a security measure used to verify a user's password when signing up for a new account. Allow the user a maximum of 4 attempts to enter the same password twice. If they succeed, display a message informing them that their account has been created. Otherwise - display a message saying their account is now locked.
	
	Enter password:	
	12345
	Enter password again:	
	123456
	Password match not found.
	You have 3 attempts remaining.
	Enter password:	
	1234
	Enter password again:	
	12345
	Password match not found.
	You have 2 attempts remaining.
	Enter password:	
	12345
	Enter password again:	
	123456
	Password match not found.
	You have 1 attempt remaining.
	Enter password:	
	12345
	Enter password again:	
	123456
	ACCOUNT LOCKED
	
	## another test run...
	
	Enter password:	
	password
	Enter password again:
	password1
	Password match not found.
	You have 3 attempts remaining.
	Enter password:
	4%fg%_&£2
	Enter password again:
	4%fg%_&£2
	ACCOUNT CREATED
	
---

### Guess My Number

5\. The magic number is 66. Write a program that allows the user a maximum of 10 attempts to guess the magic number. For each guess, feedback should be provided as follows: the program should inform the user to go "Higher" or "Lower". If the user is within 5 either side of the number, display a _"really close"_ message. Every 3 guesses, inform the user how many attempts they have left.
	
	You have 10 guesses remaining.	
	What's my magic number?	
	50	
	HIGHER!	
	What's my magic number?	
	88	
	LOWER!	
	What's my magic number?	
	80	
	LOWER!	
	You have 7 guesses remaining.	
	What's my magic number?	
	70	
	LOWER!	
	What's my magic number?	
	55	
	HIGHER!	
	What's my magic number?	
	57	
	HIGHER!	
	You have 4 guesses remaining.	
	What's my magic number?	
	62	
	really close!	
	HIGHER!	
	What's my magic number?	
	66	
	You guessed it!	

---


