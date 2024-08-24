  
# Python Challenges V

## Definite Iteration : `FOR`

---

For examples see your "Definite Iteration" worksheet on Google Drive.

_Please leave the print commands before each exercise._

---

### Cheerleader!

1\. Write a program that takes the user's name, and then prints out each letter of the person's name followed by an exclamation mark.
	
	Name?
	Bob
	B!
	o!
	b!

---

### Countdown V2

2\. Write a program that asks the user for a number to count down from. Following this the program should count down from that number until 0, and then display the message "GO!".
	
	Enter number to count down from: 7
	7
	6
	5
	4
	3
	2
	1
	0
	GO!
	
---

### Sum Kinda Program

3\. Write a program that asks the user to enter 10 numbers one by one. Following this, the program should display the total of the numbers that were entered.
	
	Enter number: 6	
	Enter number: 4	
	Enter number: 3	
	Enter number: 2	
	Enter number: 7	
	Enter number: 13	
	Enter number: 6	
	Enter number: 12	
	Enter number: 9	
	Enter number: 8	
	That's enough. Total was: 70
	
---

### Triangle

4\. Write a program that asks the user for a name and a number. Following this the program should print out the user's name in a triangle as shown:
	
	Who are you? Bob	
	How many times? 5	
	Bob	
	BobBob	
	BobBobBob	
	BobBobBobBob	
	BobBobBobBobBob	

---

## Mimicker

5\. Write a program that asks the user to enter a sentence. Afterwards it should repeat the sentence back to them a number of times based on how many characters were in the sentence. It should continuously do this until the user enters the sentence _"stop it now this is getting silly"._
	
	Enter sentence: yo	
	yo	
	yo	
	Enter sentence: what is going on?	
	what is going on?	
	what is going on?	
	what is going on?	
	what is going on?	
	what is going on?	
	what is going on?	
	what is going on?	
	what is going on?	
	what is going on?	
	what is going on?	
	what is going on?	
	what is going on?	
	what is going on?	
	what is going on?	
	what is going on?	
	what is going on?	
	what is going on?	
	Enter sentence: eh???	
	eh???	
	eh???	
	eh???
	eh???
	eh???	
	Enter sentence: stop it now this is getting silly
	OK.
	
---

### My Name, Your Name

6\. Write a program that will compare two names of equal length, letter-by-letter. The messages displayed should number each letter, and describe the letters as SAME or DIFFERENT.
	
	My name: BARRY	
	Your name: SALLY	
	Letter 1:	
	DIFFERENT	
	Letter 2:	
	SAME	
	Letter 3:	
	DIFFERENT	
	Letter 4:	
	DIFFERENT	
	Letter 5:	
	SAME
	
<!-- -->

	My name: BOB	
	Your name: OLUWAFUNMILAYO	
	I can only compare names that are the same length! Please re-enter
	My name: PRECIOUS	
	Your name: EMMANUEL	
	Letter 1:	
	DIFFERENT	
	Letter 2:	
	DIFFERENT	
	Letter 3:	
	DIFFERENT	
	Letter 4:	
	DIFFERENT	
	Letter 5:	
	DIFFERENT	
	Letter 6:	
	DIFFERENT	
	Letter 7:	
	DIFFERENT	
	Letter 8:	
	DIFFERENT
	
---

### Secret Code

7\. Write a program that asks the user for the secret code. The program should repeat until the secret code is correct. A correct secret code is one where every character falls later in the alphabet than the one previous, and the length of the secret code is no less than the square of the difference between the alphabetical positions of the first two characters. Naturally, secret codes must be at least 3 characters long.
	
	Enter secret code: zaghkls	
	That's not a secret code.	
	Enter secret code: afdeljaj	
	That's not a secret code.	
	Enter secret code: ab	
	That's not a secret code
	Enter secret code: apruvyxz
	That's not a secret code.
	Enter secret code: adeghmnuyz
	That's a secret code.
