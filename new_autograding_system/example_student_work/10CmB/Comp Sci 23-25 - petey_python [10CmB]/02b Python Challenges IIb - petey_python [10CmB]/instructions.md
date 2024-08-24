# Python Challenges IIb

## Conditional statements & logical expressions (more practice!)


---

### EXAMPLE:
	
	score = int(input("What was your score?"))
	if score >= 100:
	    print("I'm impressed! High scorer!")
	else:
	    print("Must try harder!") 
	

---

## Age Rater

1\. Write a program that informs the user about 'age milestones' they have passed. The program should begin by asking the user to input their age - it can then decide which messages should be printed in response (a maximum of **five** milestone messages).

You will need to study the automated test log carefully to work out what the exact boundaries should be.
	
	How old are you then	
	101                      ## user input
	Centenarian!
	Over the hill!	
	A quarter century!	
	Old enough to drive!	
	First word!
	How old are you then?
	39                      ## user input
	A quarter century!	
	Old enough to drive!	
	First word! 
	
---

## Even or Odd

2\. Write a program can tell the user if the number they enter is **odd** or **even.** (Reflect on "Is It A Leap Year?" for help with this).
	
	What's your number?	
	97	
	ODD!
	What's your number?
	1240
	EVEN!
	What's your number?	
	11	
	ODD!
	
---

## Word Soup

3\. Word soup is a program that takes a five-letter word as the user's input, and then changes it.

 * If the word isn't the correct length, the program prints out the word exactly as it was entered.
 * If the first letter of the word is a vowel, the program prints out the word backwards.
 * If the first letter of the word is not a vowel but is a letter that is made up straight lines only, the program prints out the first, third and fifth character of the word three times.
 * If none of the above conditions are met, the program prints out the first three characters of the word only.


<!-- -->
	
	Say your word:	
	CHEES	
	CHE
	Say your word:	
	OLIVE	
	EVILO
	Say your word:	
	TABLET	
	TABLET
	Say your word:	
	TABLE	
	TBETBETBE	
	
---

## Numberama

4\. Numberama is a program that makes comment on a three digit number entered by the user. The rules for the comments are as follows:

* If one of the three digits is larger than the sum of the other two digits, the phrase "GIANT IN THE MIDST!" is used.
* If the middle digit of the number is zero, the comment given is "HOLE IN ONE!", unless the other two digits are "1", in which case this becomes "HOLE IN ONES!".
* The comment "TRIPLETS!" is used to describe a number with all three digits the same, but otherwise - the comment "CORNERED!" is used when two of the three digits are the same.
* If the sum of all of the digits is bigger than 15, the phrase "A HAPPY MEDIUM!" is given.

<!-- -->
	
	ENTER YOUR NUMBERAMA:	
	333	
	TRIPLETS!
	ENTER YOUR NUMBERAMA:	
	911	
	GIANT IN THE MIDST!	
	CORNERED!
	ENTER YOUR NUMBERAMA:	
	123	
	NO COMMENT.
	
 ---
