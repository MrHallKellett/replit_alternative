  
# Python Challenges X

_Understanding user-defined functions and procedures._

_Defining a function:_
	
	def my_function(param1, param2):
	
	    ## do stuff
	    return result_variable
	
_Calling a function:_
	
	x = my_function(arg1, arg2)
	##OR
	print(my_function(arg1, arg2)
	##OR
	if my_function(arg1, arg2) == True:
	
	    ## do some conditional stuff
	##OR
	another_function(my_function(arg1, arg2)) 
	
A **function** is a reusable block of code that has data passed into it as **arguments** when **called**.

Each item of data is then accepted as a **parameter** inside the function - but this truly is only a copy of the original data!

This is why in order to get the data back OUT of the function you must use global variables (ill-advised 99% of the time) or preferably... use the **`return`** keyword and make sure the function call is assigned to a variable when made.

If a return statement is NOT used, the function does not need to be assigned to a variable. This type of subroutine is known as a 'procedure'  - and typically will result in the data being processed and then printed to the console instead (or output in some other way, for example written to a file or database).
	
	def cool_maths(num1, num2):
	
	    num3 = num1 + num2
	    print(num3)
	
Above I have defined a procedure named `cool_maths()`. The procedure accepts two parameters: `num1` and `num2`.
	
	answer = cool_maths(num1, num2)
	print(answer)
	
Typically I might call a function using this format. But because this is a procedure, the print(answer) line would result in the console outputting:
	
	None
	
Watch out for this error! If the exception raised describes a 'NoneType' it may be to do with the fact you have missed out the return statement.
	
	def you_confused(a_thing, another, something_else="")
	
	    if a_thing > 10:
	
	        return another + another
	    else:
	
	        return something_else + (another * a_thing)
	
Don't get caught out. Functions can be called using variables, literal values or even other functions. In this example I have defined a function named `you_confused()` that accepts three parameters. The final argument - `something_else` - is an optional parameter that defaults to an empty string when missed out.
	
	## calling a function with literals
	result = you_confused("hello", 6)
	## calling a function with variables
	word = input()
	num = len(word)
	result = you_confused(word, num, "!!!")
	
In the second example here the value of `something_else` will be `"!!!"`, as an argument _was_ given when called.
	
	## calling a function with functions that return data!
	result = you_confused(another_function(stuff), sum(nums), "?")
	
# ----------

# Tasks

# ----------


---

## There are two functions that are already defined - make sure these are left intact - do not change the code from line 1 to line 50!

1\. Call the `make_silly_name()` function with the name "bob marley". Print the result to the user.

2\. Ask the user to input a name and store this in a variable. Now, call the `make_silly_name()` function with the user's name and then print out the result.

3\. Define a function called `make_serious_name()` that takes a name as a parameter and returns a variable named `serious_name`.

To decide the value of `serious_name` do the following:

- If the name entered is longer than 10 characters, add the prefix "Mrs. " to the name.

- If the name is shorter than 11 characters and starts with a letter in the first half of the alphabet, add the prefix "Mr. " to the name.

- If the name is shorter than 11 characters and starts with a letter in the last half of the alphabet, add the prefix "Dr. " to the name.

- If the name starts with a non-alphabetical character, add the prefix "Master" to the name.

- Make all characters in the name (apart from the prefix you just added) UPPERCASE.

4\. Finally, finish defining the procedure called `name_menu()`.

Inside this procedure, start by asking the user to enter their name and store this in a variable.

Present them with the following options, calling each function as necessary.
	
	ENTER 1 TO MAKE A SILLY NAME
	ENTER 2 TO MAKE A SERIOUS NAME
	ENTER 3 TO MAKE AN ABBREVIATED NAME
	
At the end of the procedure output the user's new name in the following format:
	
	Your new name is: crs
	
To test that this works, call the `name_menu()` procedure **three** times in sequence at the end of the program.

