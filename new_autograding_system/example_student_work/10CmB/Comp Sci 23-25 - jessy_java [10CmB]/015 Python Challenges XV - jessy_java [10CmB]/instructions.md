# Python Challenges XV

## Validation and Verification

---

**Context:** You have designed the most exciting new website. Users are signing up - but you need to make sure the data they input makes sense.

_Named CONSTANTS should be used throughout this task wherever appropriate._

_All code must be fully #commented explaining the processes taking place._

---

### Task 1: Type check

Ask the user to enter a secret (positive and whole) number. Validate before continuing, and then once the input is valid display the message "`Your secret number is set to X"` and return the secret number.

---

### Task 2: Presence Check

Ask the user to enter their forename. Any characters are allowed, and the minimum length is 1. Validate before continuing, and then once the input is valid display the message `"Your name is set to X"` and return the name.

---

### Task 3: Range Check

Ask the user to confirm their age. The minimum age for users is 13. Validate before continuing, and then once the input is valid display the message `"Your age is set to X".` and return the age.

---

### Task 4: Format check

Ask the user to enter their verification code. Their verification code must be in the format [digit][any non-non printing (visible) ASCII character][digit][uppercase letter][lowercase letter]. Validate before continuing, and then once the input is valid display the message `"Your verification code is set to X."` and return the code.

---

### Task 5: Unique check

Ask the user to enter their username. It must not match any username already taken in the system. Validate before continuing, and then once the input is valid display the message `"Your username is set to X".` and return the updated username list.

---

### Task 6: Length check

Ask the user to enter their password. The minimum length is 6, and the maximum length is 24. Validate before continuing, and then once the input is valid display the message `"Your password is set to X".` and return the password.

---

### Task 7: Double entry check

Ask the user to re-enter their password. And then ask the user to re-enter their password again. Repeat this until it has been verified that both passwords match. Once this is complete, display the message `"Password verified".` and return `True`.

---

### EXTENSION TASK 1: Similarity check

---

A Python library exists that allows you to check the similarity between two strings - Google this. Modify your code for TASK 5 so that any username cannot be more than 75% similar to a username that has already been taken.

---

### EXTENSION TASK 2: Data input from calendar

Explore PyQT , tkinter or another GUI framework. Create a program that allows the user to enter their date of birth from a date input UI and then displays the message `"Only X days until your next birthday!!!".` You will need to do this in a local Python IDLE project.

---