
# Python Challenges Vb

## Nested FOR loops


---

For each exercise, study the output shown. How can you use nested `for` loops (a loop inside a loop) to generate this output? Modify the exemplar solution shown for Task 1 to complete each task.


---

**Please note - using any string longer than 1 character defeats the point of this exercise.**


---

Task 1 (an exemplar)

		
	*
	**
	***
	****
	*****
	******
	*******

---

**SOLUTION**

	
	# loop 7 times starting at 1	
	for i in range(1, 8):	
	  # loop i times	
	  for j in range(i):	
	    # output star on same line	
	    print("*", end="")	
	  # print a new line	
	  print()
	
---

### Task 2

	
	***********	
	**********	
	*********	
	********	
	*******	
	******	
	*****	
	****	
	***	
	**	
	*
	
---

### Task 3

	
	**
	****
	******
	********
	**********
	
---

### Task 4

	
	0123456789	
	0123456789	
	0123456789	
	0123456789	
	0123456789	
	0123456789	
	0123456789	
	0123456789	
	0123456789	
	0123456789
	
---

### Task 5

	
	
	*
	**
	****
	********
	****************
	********************************

---

### Task 6

	
	0123456789	
	012345678
	01234567	
	0123456	
	012345	
	01234	
	0123	
	012	
	01	
	0
	

---

### Task 7

	
	0000000000	
	1111111111	
	2222222222	
	3333333333	
	4444444444	
	5555555555	
	6666666666	
	7777777777	
	8888888888	
	9999999999	

---

### Task 8

	
	0	
	01	
	012	
	0123	
	01234	
	012345	
	0123456	
	01234567	
	012345678	
	0123456789
	

---

### Task 9

	
	0123456789	
	 012345678	
	  01234567	
	   0123456	
	    012345	
	     01234	
	      0123	
	       012	
	        01	
	         0
	
---

### Task 10

	
	         0	
	        010	
	       01210	
	      0123210	
	     012343210	
	    01234543210	
	   0123456543210	
	  012345676543210	
	 01234567876543210	
	0123456789876543210	

---

### Task 11

	
	0000	
	1 1 1 1	
	2  2  2  2	
	3   3   3   3	
	4    4    4    4	
	5     5     5     5	
	6      6      6      6	
	7       7       7       7	
	8        8        8        8	
	9         9         9         9	