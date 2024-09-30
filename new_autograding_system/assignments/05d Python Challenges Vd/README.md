# Y8 Coding Week 5: Loopy Learning

## Debugging FOR Loops

---	
	
	## TASK 1
	for i in range(5):	
	    print("Bob")
	
Copy the code above into the code editor and press run. This runs a loop that will print the string `"Bob"` 5 times!

---	
	
	## TASK 2
	for j in range(7):	
	    print("🍜 Noodles")
	print("🍚 Rice")         # this is OUTSIDE of the loop.
	
Copy the code above into the code editor and press run. This loop runs 7 times, printing "Noodles" each time. After the loop is finished, "Rice" is printed.

---	
	
	## TASK 3
	for j in range(3):	
	    print("🦖 Dinosaur")
	print("🐘 Elephant")   
	
Copy the above code into the editor and press run.

Can you change this loop so that instead of printing "Dinosaur" 3 times and "🐘 Elephant" once... "Dinosaur" and "🐘 Elephant" are both printed 3 times?
	
	CURRENT OUTPUT:               EXPECTED OUTPUT:
	>= '🦖 Dinosaur'              >= '🦖 Dinosaur'
	>= '🦖 Dinosaur'              >= '🐘 Elephant'
	>= '🦖 Dinosaur'              >= '🦖 Dinosaur'
	>= '🐘 Elephant'              >= '🐘 Elephant'
	                              >= '🦖 Dinosaur'
	                              >= '🐘 Elephant'
	
---	
	
	## TASK 4
	for x in range(3):
	
	    print("🐱 Cat")
	    print("🐶 Dog")   
	
Can you change this loop so that instead of "🐶 Dog" and "🐱 Cat" being printed 3 times, "🐶 Dog" is printed 6 times and then "🐱 Cat" is printed once?
	
	CURRENT OUTPUT:               EXPECTED OUTPUT:
	>= '🐶 Dog'                      >= '🐶 Dog'
	>= '🐱 Cat'                      >= '🐶 Dog'
	>= '🐶 Dog'                      >= '🐶 Dog'
	>= '🐱 Cat'                      >= '🐶 Dog'
	>= '🐶 Dog'                      >= '🐶 Dog'
	>= '🐱 Cat'                      >= '🐶 Dog'
									 >= '🐱 Cat'
	
---	
	
	## TASK 5
	for x in range(4):
	
	    print("🐸 Frog")
	
Can you change this loop so that instead of "🐸 Frog" being printed four times, "🐁 Mouse" is printed once, then "🐸 Frog" is printed four times and then "🐎 Horse" is printed once?
	
	CURRENT OUTPUT:               EXPECTED OUTPUT:
	>= '🐸 Frog'                      >= '🐁 Mouse'
	>= '🐸 Frog'                      >= '🐸 Frog'
	>= '🐸 Frog'                      >= '🐸 Frog'
	>= '🐸 Frog'                      >= '🐸 Frog'
	                                  >= '🐸 Frog'
	                                  >= '🐎 Horse'
	
---	
	
	## TASK 6
	for x in range(2):
	
	print("🐶 Dog")
	print("🐱 Cat")
	
This loop contains a syntax error. Can you fix the error to get the expected output?
	
	EXPECTED OUTPUT:
	>= "🐶 Dog"
	>= "🐱 Cat"
	>= "🐶 Dog"
	>= "🐱 Cat"
	
---	
	
	## TASK 7
	for x in range(3):
	
	    print("🦒 Giraffe")
	        print("🐒 Monkey")
	
This loop contains a syntax error. Can you fix the error to get the expected output?
	
	EXPECTED OUTPUT:
	>= '🦒 Giraffe'
	>= '🐒 Monkey'
	>= '🐒 Monkey'
	>= '🐒 Monkey'
	
---	
	
	## TASK 8
	for x in range(1):
	
	    print("🐯 Tiger")
	    print("🦁 Lion")
	    print("🐯 Tiger")
	
This program doesn't need a loop. Remove the FOR line of code and fix the indentation before the prints and the program will do exactly the same thing!

---	
	
	## TASK 9
	print("🙈 Chimp")              ## before BOTH loops begin
	for x in range(3):	
	    for y in range(3):	
	        print("🦔 Hedgehog")   ## inside the inner loop
	    print("🐮 Cow")            ## outside of the inner loop, but in the outer loop!
	print("🦍 Gorilla")            ## after BOTH loops have ended
	

---

TASK 9 contains a nested loop. Copy and paste this into the code editor and run the code to work out what it does!

---	
	
	## TASK 10
	for i in range(2):	
	    for j in range(2):	
	        print("🐍 Snake")
	    print("🦎 Lizard")
	
Can you fix this nested loop? You must keep BOTH for loop statements in your code!
	
	CURRENT OUTPUT:        EXPECTED OUTPUT:
	>= '🐍 Snake'             >= '🐍 Snake'
	>= '🐍 Snake'             >= '🦎 Lizard'
	>= '🦎 Lizard'            >= '🐍 Snake'
	>= '🐍 Snake'             >= '🦎 Lizard'
	>= '🐍 Snake'             >= '🐍 Snake'
	>= '🦎 Lizard'            >= '🦎 Lizard'
	                          >= '🐍 Snake'
	                          >= '🦎 Lizard'
	
---	
	
	## TASK 11
	print("🐇 Bunny")
	for i in range(2):	
	    for j in range(2):	
	        print("🐰 Rabbit")
	print("🐹 Hamster")
	
Can you fix this nested loop? You must keep BOTH for loop statements in your code!
	
	CURRENT OUTPUT:        EXPECTED OUTPUT:
	>= '🐇 Bunny'             >= '🐹 Hamster'
	>= '🐰 Rabbit'            >= '🐇 Bunny'
	>= '🐰 Rabbit'            >= '🐇 Bunny'
	>= '🐰 Rabbit'            >= '🐰 Rabbit'
	>= '🐰 Rabbit'            >= '🐇 Bunny'
	>= '🐹 Hamster'           >= '🐇 Bunny'
	                          >= '🐰 Rabbit'
	
---	
	
	## TASK 12
	for i in range(5):	
	    print("🐧 Penguin")   
	    for j in range(2):	
	        print("Macaque")
	print("🦉 Owl")
	
Can you fix this nested loop?
	
	CURRENT OUTPUT:        EXPECTED OUTPUT:
	>= '🐧 Penguin'          >= '🐧 Penguin'
	>= '🐔 Chicken'          >= '🐔 Chicken'
	>= '🐔 Chicken'          >= '🐔 Chicken'
	>= '🐧 Penguin'          >= '🐔 Chicken'
	>= '🐔 Chicken'          >= '🦉 Owl'
	>= '🐔 Chicken'          >= '🐧 Penguin'
	>= '🐧 Penguin'          >= '🐔 Chicken'
	>= '🐔 Chicken'          >= '🐔 Chicken'
	>= '🐔 Chicken'          >= '🐔 Chicken'
	>= '🦉 Owl'              >= '🦉 Owl'
	
---	
	
	## TASK 13
	print("🐱 Cat")
	for i in range(3):	
	    print("🐱 Cat", "🐶 Dog")   
	    for j in range(3):	
	        print("🐶 Dog")
	
Can you fix this nested loop?
	
	CURRENT OUTPUT:        EXPECTED OUTPUT:
	>= '🐱 Cat'               >= '🐶 Dog'
	>= '🐱 Cat 🐶 Dog'        >= '🐶 Dog'
	>= '🐶 Dog'               >= '🐶 Dog'
	>= '🐶 Dog'               >= '🐶 Dog 🐱 Cat'
	>= '🐶 Dog'               >= '🐱 Cat'
	>= '🐱 Cat 🐶 Dog'        >= '🐱 Cat 🐱 Cat'
	>= '🐶 Dog'               >= '🐱 Cat 🐱 Cat'
	>= '🐶 Dog'               >= '🐶 Dog'
	>= '🐶 Dog'               >= '🐶 Dog'
	>= '🐱 Cat 🐶 Dog'        >= '🐶 Dog'
	>= '🐶 Dog'               >= '🐶 Dog 🐱 Cat'
	>= '🐶 Dog'               >= '🐱 Cat'
	>= '🐶 Dog'               >= '🐱 Cat 🐱 Cat'
	                          >= '🐱 Cat 🐱 Cat'
	
---	
	
	## TASK 14
	
Use a nested loop to display this output.
	
	EXPECTED OUTPUT:
	>= '🐐 Goat'
	>= '🐑 Sheep'
	>= '🐑 Sheep'
	>= '🐐 Goat'
	>= '🐐 Goat'
	>= '🐐 Goat'
	>= '🐐 Goat'
	>= '🐑 Sheep'
	>= '🐑 Sheep'
	>= '🐐 Goat'
	>= '🐐 Goat'
	>= '🐐 Goat'
	>= '🐐 Goat'
	>= '🐑 Sheep'
	>= '🐑 Sheep'
	>= '🐐 Goat'
	>= '🐐 Goat'
	>= '🐐 Goat'
	