# Python Challenges VI

## Lists


Lists (Python's extendable arrays) are used to form collections of data. These are useful in many ways that will become apparent as you work through this problem set.


---


	## Declaring a list:
	my_list = ["test", "hello", "chicken"]


---


	## Adding something on to the end of the list:
	my_list .append("something")  # this could also be a variable,
	                           # or any type of data


---


	## Accessing a single part of the list (indexing / 'subscription'):
	word = my_list[2]   # the index can also be a variable
	print(word)

_You will need to continue to use **loops** to effectively solve these challenges._


---

## Sports Recorder

1\. Write a program that allows the user to enter the names of five different sports, and then displays a list of sports back to them at the end.

	Enter sport: football
	Enter sport: tennis
	Enter sport: badminton
	Enter sport: table tennis
	Enter sport: judo
	Your sports were:
	['football', 'tennis', 'badminton', 'table tennis', 'judo']


---

## My Zoo

2\. Ask the user to enter a word. Use a membership test to check if the word is one of the 3 letter animals: _cat, dog, cow, pig, rat, bat, ewe_. If the animal is, inform the user. If the animal is not found, report ‘not found’. _Make this program loop until the user enters a valid animal._

	What animal?
	donkey
	Not one of mine.
	What animal?
	marmoset
	Not one of mine.
	What animal?
	cat
	That’s one of mine!


---

## Name Positions

3\. Write a program that contains a list of 10 names:

_Baz, Beth, Mik, Dave, Bill, Chuck, Olu, Ted, Dewan, Anjel._

Ask the user to input a number between 1 and 10. The program should then find the name that corresponds to the number, and prints out this information (name in uppercase) for the user. Make the program repeat until a valid number is chosen.

	What number?
	-55
	Please enter between 1 and 10 only.
	What number?
	11
	Please enter between 1 and 10 only.
	What number?
	MIK was found at number 3


---

## Length of Friends

4\. Write a program that allows the user to input a list of names - the program should repeatedly ask for a name to be entered UNTIL the user enters the word ‘_stop_’. Each time a name is entered, make the program calculate the length of the name - and add this to a list. When the user enters ‘_stop_’, the program should output a list of the name lengths before terminating.

	What name?
	Jones
	What name?
	Aki
	What name?
	Daniel
	What name?
	Susannah
	What name?
	stop
	OK - stopping. The names you entered had these lengths:
	[5, 3, 6, 8]


---

## Word Analysis Table

5\. Create a program to analyse a list of words entered by the user:

- Begin this program by asking the user for a number. This will then decide how many words will be entered.
- Ask the user to enter a number of words, adding each one to a list.
- Use a loop to iterate through the table headings and print them out evenly on the screen.
- Use a loop to iterate through each word in the list and display the necessary information - number of letters, number of vowels, number of letters that occur more than once.
- You will need to use the length of the longest word in the list to decide how to evenly space the first column in the table.


Required user interface:

	How many words to analyse?
	OK - I will analyse 7 words.
	Enter word 1:  banana
	Enter word 2:  chicken
	Enter word 3:  frog
	Enter word 4:  lemon
	Enter word 5:  elephant
	Enter word 6:  dinosaur
	Enter word 7:  unbelievable
	WORD ANALYSIS
	WORD         LETTERS VOWELS REPETITIONS
	banana       6       3      2
	chicken      7       2      1
	frog         4       1      0
	lemon        5       2      0
	elephant     8       3      1
	dinosaur     8       4      0
	unbelievable 12      6      3

