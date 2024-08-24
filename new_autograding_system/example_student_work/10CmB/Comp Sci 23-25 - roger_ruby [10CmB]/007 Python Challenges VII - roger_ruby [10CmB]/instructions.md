# Python Challenges VII

## _File IO_

---

In order to save data between program executions it must be written to - and then read from - secondary storage. To understand a basic implementation of this you will be writing programs that interact with .txt text files.


---

## TASK 1:

Create a text file named "my_data.txt" - remember to close it after creating it!

---

## TASK 2:

Write the words "banana", "apple" and "pineapple" to the text file on separate lines.

---

## TASK 3:

Allow the user to input the name of a new text file. If they forget to add '.txt', make sure your program adds this for them. Create this file, close it, and then return the filename from the `task3()` function.

---

## TASK 4:

Open the newly created text file and allow the user to write 10 different words to it on different lines.

To do this you should configure `task4()` so that it accepts a single parameter - filename (string). Modify the procedure's header to enable this.

---

## TASK 5:

Open the two text files in read mode. Iterate through the lines in each file and display the text from each on the same line - _see example below._
	
	FILE 1        FILE 2
	banana        ramkamhaeng
	apple         chan
	pineapple     sathon
	
---

## TASK 6:


---

## Define the following functions to complete this task:
	
	find_prime(max: int)                    ## returns a list of prime numbers up to max
	find_square(n: int)                     ## returns a list of square numbers, n items long
	copy_nth_line(file_lines: list, n: int) ## copies every nth line from file_lines into a file named copy.txt
	
Add 60 to each of the first 5 prime numbers, convert each into an ASCII character and use this a filename - create a new file with this filename. Write the first 100 square numbers to the file, each on a separate line.

Create a second file named copy.txt and have it open in write mode. Open the file created above in read mode and iterate through the lines in the file. Copy every 7th line from the original file into the file copy.txt.

---

## TASK 7:

Find 3 examples of pseudocode file handling from the past papers folder - you can search for the keyword OPENFILE to do this.

Store each pseudocode example as a multiline string.

Convert each pseudocode example into working Python code - showing your understanding of the Python vs. pseudocode conversion table on line 13 of the lesson slides.