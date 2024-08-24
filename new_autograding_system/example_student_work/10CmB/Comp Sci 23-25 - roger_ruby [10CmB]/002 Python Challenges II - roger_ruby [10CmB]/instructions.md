---

<p style="background-color:#b2fa96; text-align:center; border-radius:15px; margin-bottom:3em;"><b>NOTICE</b>: This problem set was altered on 13/09/2022. To make sure the automated tests still pass: copy and paste the code below into your main method</p>

<!-- -->


    #####################################################################

    # leave this block of code as it is!

    if __name__ == "__main__":


    	print('''Enter 1 to test OLD ENOUGH TO DRIVE
    Enter 2 to test GRADE CALCULATOR
    Enter 3 to test LEAP YEAR
    Enter 4 to test FINANCIAL ADVISER
    Enter 5 to test NAME LENGTH COMPARISON
    Enter 6 to test USERNAME VALIDATOR''')

    	x = input()
    	if x in "123456":
    		[old_enough_to_drive,
    		grade_calculator,
    		leap_year,
    		financial_adviser,
    		name_length_comparison,
    		username_validator][int(x)-1]()

<!-- -->



# Python Challenges II

## Conditional statements & logical expressions

---

### EXAMPLE:

	name = input("Who are you?")
	if name == "Freddy":
	    print("We've been expecting you, come in…")
	else:
	    print("Who are you?")


---

## Are You Old Enough to Drive?

1\. Write a program that asks the user their age, then tells them if they are old enough to drive.

	How old are you then?
	14                          ## user input
	Too young to drive.
	How old are you then?
	91
	Old enough to drive!

---

## Grade Calculator

2\. Write a program that asks the user to input their test score out of 100, it then tells them what grade they will receive - based on these grade boundaries:

<ul>
<li>A* > 87</li>
<li>A > 77</li>
<li>B > 70</li>
<li>C > 63</li>
<li>D > 57</li>
<li>E > 50</li>
</ul>

<!-- -->
	Enter mark:
	55                           ## user input
	That's a grade E.
<!-- -->
---

## Is It A Leap Year?

3\. Write a program that asks the user to input a year in the format YYYY. The program will then tell the user if the year was/is going to be a leap year in the western calendar.

You will need to recap the modulo operator to complete this activity.

	What year? 1945
	Not a leap year
	What year? 2016
	That one's a leap year!

---

## Financial Adviser

4\. Create a program that provides the following financial advice: A packet of crisps costs 70p. Having £100 or more in the bank is living comfortably. BUT if you're a millionaire, you're a millionaire... and if there's over a billion in the bank... well then you're a billionaire.

You will need to recap the float data type to complete this activity.

	How much is in the bank? £0.50
	No crisps for you!
	How much is in the bank? £0.76
	Barely enough for a packet of crisps!
	How much is in the bank? £1000101
	You're a millionaire!
	How much is in the bank? £3123456845
	You're a billionaire!
	How much is in the bank? £15468
	Living comfortably.

---

## Name Length Comparison

5\. Write a program that asks the user to enter their first name and their second name. It then should tell them which is longer, by how many letters.

	What's your forename?
	Jemimi                                  ## user input
	What's your surname?
	Boggleberry                             ## user input
	Your surname is longer by 5 characters.
	What's your forename?
	Oluwafunmilayo
	What's your surname?
	Oyedepo
	Your forename is longer by 7 characters.

---

## Username Validator

6\. Write a program that asks the user to enter a new username. If the username they enter is valid, display a message saying that it is successful.

- Valid usernames must:
- Be between 10 and 18 characters
- Not include any spaces
- The first letter must be "X"

<!-- -->

	Enter username:
	michaelschumacher1945
	Invalid. Try again
	Enter username:
	michaelschumacher
	Invalid. Try again
	Enter username:
	Xmichaelschumacher
	Valid. Username accepted

