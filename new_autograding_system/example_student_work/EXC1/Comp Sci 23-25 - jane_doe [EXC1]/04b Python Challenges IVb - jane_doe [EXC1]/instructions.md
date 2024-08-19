  
# Python Challenges IVb

## Indefinite iteration - More WHILE loop challenges

---

**Example**

	
	## repeat until the word entered starts with a "b".
	word = input("Word? ")
	
	while word[0] != "b":
	    word = input("Please let it b.... ")
	print("B gone with you.")
	

---

## Contain A 'z'?

1\. Write a program that repeatedly asks the user "HOW MANY Zs?" until the user enters a word that contains the letter "z". When this happens, make the program print the phrase "GOTCHA."

	
	HOW MANY Zs?	
	nothing...	
	HOW MANY Zs?	
	what?	
	HOW MANY Zs?	
	tuvwxy...	
	HOW MANY Zs?	
	zebra	
	GOTCHA
	
---

## It Was A Good Year.

2\. The program's favourite decade was the 1950s. Repeatedly ask the user to enter a year until it is one of the program's favourite years.

	
	Enter year:	
	1949	
	Enter year:	
	2001	
	Enter year:	
	2017	
	Enter year:	
	1959	
	It was a good year.
	
---

## 100 Letter Story

3\. Ask the user to tell the program a story. The story is 'not good enough' until it contains at least 100 characters.

	
	Tell me a story:	
	Once upon a time a Python developer was caught using Internet Explorer...	
	NOT GOOD ENOUGH	
	Tell me a story:	
	A long time ago in a namespace far, far away...	
	NOT GOOD ENOUGH	
	Tell me a story:	
	There once was a young boy named JavaScript who had many, many friends - most of whom were brackets.	
	GOOD ENOUGH	

---

## Instrument Doubler

4\. Ask the user to type in the name of their favourite musical instrument. Repeatedly duplicate the name of the instrument 6 times in a loop:

	
	Favourite instrument?	
	Guitar	
	OK!	
	GuitarGuitar	
	GuitarGuitarGuitar	
	GuitarGuitarGuitarGuitar	
	GuitarGuitarGuitarGuitarGuitar	
	GuitarGuitarGuitarGuitarGuitarGuitar	
	GuitarGuitarGuitarGuitarGuitarGuitarGuitar	

---

## Indefinite Adding

5\. Ask the user for two numbers. Add the numbers together and remember the result. Keep adding the first number to the result until it exceeds 1000. After this, display the _product_ of the original two numbers.

	
	Enter number 1:	
	77	
	Enter number 2:
	44
	Here we go!	
	77 + 44 = 121	
	77 + 121 = 198	
	77 + 198 = 275	
	77 + 275 = 352	
	77 + 352 = 429	
	77 + 429 = 506	
	77 + 506 = 583	
	77 + 583 = 660	
	77 + 660 = 737	
	77 + 737 = 814	
	77 + 814 = 891	
	77 + 891 = 968	
	77 + 968 = 1045 	
	PRODUCT:	
	3388
	
