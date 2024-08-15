# Python Challenges VIII

## Random

---

<!-- -->
	from random import choice, randint, randrange, shuffle, sample
<!-- -->
	
The `random` library contains several functions that will be helpful for you.

<ul>
<li><code>choice(items)</code> -> returns one random item from a list of items</li>
<li><code>randint(min, max)</code> -> generates a random integer between a min and max, inclusive</li>
<li><code>randrange(min, max)</code> -> generates a random integer between a min and max, exclusive of the upper bound</li>
<li><code>shuffle(items)</code> -> randomises the order of a list of items</li>
<li><code>sample(items, n)</code> -> returns <code>n</code> items at random from a list of items</li>
</ul>

Python also has some built-in functions for converting numbers that will help you too!

<ul>
<li><code>hex(n)[2:]</code> -> convert <code>n</code> into hexadecimal.</li>
<li><code>bin(n)[2:]</code> -> convert <code>n</code> into binary.</li>
<li><code>int(n, 2)</code> -> convert the binary number <code>n</code> into denary.</li>
<li><code>int(n, 16)</code> -> convert the hex number <code>n</code> into denary.</li>
</ul>

---

## Random Number Base Quiz

### Task 1

Your Task is to create a random number base conversion quiz, to help you to practise converting between binary/hexadecimal/denary for your Paper 2 examination.
	
	Convert the binary number 111 to denary:
	7
	Correct!
	You have 1 point.
	
	Convert the denary number 17 to binary:
	10001
	Correct!
	You have 2 points.
	
	Convert the hexadecimal number A0 to denary:
	161
	Incorrect. The correct answer was 160!
	You have 1 point.
	
	Convert the binary number 11011 to denary:
	27
	Correct!
	You have 2 points.

Follow the structured English guide below to help you to do this:

<ol>
<li>Make the program pick a random option number between 1 and 4 and store it in a variable.</li>
<li>Create a random denary number between 10 and 256 and store it another variable.</li>
<li>If the random option chosen was number 1, the program will ask the user to convert binary to denary.. so:</li>
<li>Store the random number as the correct answer.</li>
<li>Convert the correct answer to binary and create the question using the binary number. Store this in a variable named `question`.</li>
<li>If the random option chosen was number 2, the program will ask the user to convert denary to binary.</li>
<li>Convert the random number to binary and store this as the correct answer.</li>
<li>Create the question using the random number and store this in a variable.</li>
<li>If the random option chosen was number 3, the program will ask the user to convert hexadecimal to denary.</li>
<li>Store the random number as the correct answer.</li>
<li>Convert the correct answer to hexadecimal and create the question using the hexadecimal number.  Store this in a variable named `question`.</li>
<li>If the random option chosen was number 4, the program will ask the user to convert denary to hexadecimal.</li>
<li>Convert the random number to hexadecimal and store this as the correct answer.</li>
<li>Create the question using the random number and store this in a variable.</li>
<li>Display the question to the user.</li>
<li>Get the user's answer.</li>
<li>Check the user's answer against the correct answer.</li>
<li>If the user's answer is correct, award 1 point.</li>
<li>If the user's answer is incorrect, deduct 1 point.</li>
<li>Display the user's points.</li>
<li>If the user has not yet reached 10 points go back to step 1.</li>
</ol>
</li>

---

### Task 2

Extend your quiz to include hexadecimal-to-binary and binary-to-hexadecimal questions too.

	Convert the binary number 11110101 to hexadecimal:
	F5
	Correct!
	You have 3 points.
	
	Convert the hexadecimal number 17 to binary:
	00010111
	Correct!
	You have 4 points.
	
---

### Task 3

Extend your program into a 2-player game. Allow the users to enter their names at the start of the game, and have the program record the points for each user separately.

	Player 1 enter your name: Worakarn
	Player 2 enter your name: Abhjeet
	
	Worakarn, it's your turn!

	Convert the denary number 17 to hexadecimal:
	11
	Correct!
	You have 1 point.
	
	Abhjeet, it's your turn!
	
	Convert the hexadecimal number EC to binary:
	1111100
	Incorrect. The correct answer was: 11101100
	You have 0 points.

---
	
### Task 4

Modify your game so the user needs 20 points to complete the quiz instead of just 10.

Introduce **stages** into your game:

The game starts on stage 1 - where the random numbers generated are between 10 and 16.

The user needs 3 points to progress to the next stage.

Each time the user moves to the next stage, the maximum number that can be generated doubles:

<ul>
<li><code>STAGE 2</code> - random numbers between 10 and 32</li>
<li><code>STAGE 3</code> - random numbers between 10 and 64</li>
<li><code>STAGE 4</code> - random numbers between 10 and 128</li>
<li><code>STAGE 5</code> - random numbers between 10 and 256</li>
</ul>

Inform the user each time they progress to the next stage.

---

### EXTENSION (Grade 9)

All number bases follow a common format when converting numbers to or from denary.

<ul>
<li>The rightmost column (index 0) is always worth 1, because <em>any number</em> to the power of 0 = <b>1</b>.</li>
<li>The second column (index 1) is always worth <code>n</code>, because <em>any number</em> to the power of 1 = <pre>n</pre>.</li>
<li>The third column (index 2) is worth <code>n squared</code> = <em>(n to power of 2)</em>.</li>
<li>The fourth column (index 3) is worth <code>n cubed</code> <em>(n to power of 3)</em>.</li>
</ul>

Consider **quaternary**, or the base-4 number system, which uses *four* possible digits: `0`, `1`, `2` and `3`:

	
	Column index:	|	5	|	4	|	3	|	2	|	1	|	0	|
	Calculation:	|	4⁵	|	4⁴	|	4³	|	4²	|	4¹	|	4º	|
	Column value:	|	1024| 	256 |	64	|	16 	|	4	|	1	|
	-------------------------------------------------------------
	Example:		|	3	|	3	|	2	|	0	|	0	|	1	|
	
	
The quaternary number **332001** = **3969** in denary because:
	
	(3 x 1024) + (3 x 256) + (2 x 64) + 1 = 3969
	
Define a function named `convert()` that takes `start_base` and `end_base` as parameters.

Program your function so it is able to convert any number from the given `start_base` into the given `end_base`.

Utilise your function in the quiz game once the user reaches **stage 6**.

	Convert the hexadecimal number 17 to binary:
	00010111
	Correct!
	You have 15 points.
	
	STAGE 6!
	
	Convert the quinary number 444 to ternary:
	11121
	Correct!
	You have 16 points.
	
	Convert the nonary number 518 to dozenal:
	2B2
	Correct!
	You have 17 points.

---




