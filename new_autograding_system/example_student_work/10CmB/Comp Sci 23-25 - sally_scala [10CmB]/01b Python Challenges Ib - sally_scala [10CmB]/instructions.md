#  Python Challenges Ib

## Input, output, variables and assignment EXTENSION


---

### L33t sp34k

The `.replace()` function can be used to replace any instance of  letter in a word with another.

Have a look at the example below, what would be printed to the console?
	
	animal = "elephant"
	animal = animal.replace("e", "o")
	print(animal)
	
1\. 1337sp34k is a form of (early) internet language where users replace certain letters with numbers or other special characters. What characters can you think of? `3` commonly replaces `e`, `4` commonly replaces `A`. `|<` is sometimes used for the letter `K`.

It's also important that any punctuation used is repeated 3 times.

_See below for an example._

Can you create a program that translates the user’s input into 1337sp34k?
	
	Say something:
	this is how all the cool people on the internet talk!
	7|-|!5 !5 |-|0\/\/ 411 7|-|3 c001 p30p13 0n 7|-|3 !n73rn37 741|<!!!
	Say something:
	omg! how are you?
	0mg!!! |-|0\/\/ 4r3 y0u???
	
---

### Banner

2\. Write a program that prints a banner for the user. The output shown below is taken from two examples - a user named "Ted" and a user named "Kanye West". The program should be reusable - the banner should resize according to the length of the user’s name - pay special attention to the correlation between the number of symbols and the length of the user's name.
	
	Who are you? Kanye West
	----------==============----------
	--------/ / KANYE WEST \ \--------
	----------==============----------
	Who are you? Ted
	---=======---
	-/ / TED \ \-
	---=======---
	
p.s. `.upper()` can be used to convert a string into uppercase.

---

### Grid

3\. Create a program that  will print a grid to the screen. Try to make your code as efficient/short as possible - remember the `*` operator and the syntax for new line: `\n`. The grid must resize according to the examples shown below:
	
	What size grid?
	*-*-*-*-*-*-*-*
	| | | | | | | |
	*-*-*-*-*-*-*-*
	| | | | | | | |
	*-*-*-*-*-*-*-*
	| | | | | | | |
	*-*-*-*-*-*-*-*
	What size grid?
	*-*-*-*
	| | | |
	*-*-*-*
	
