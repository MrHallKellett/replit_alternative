from random import choice, randint, randrange, shuffle, sample

question = random.randint(1,4)
first_num = randint(10, 256)
score = 0
if num == 1:
    rand_ans = bin(random_num)[2:]
    user_input = int(input(f"Convert the binary number {rand_ans} to denary"))
    ans = first_num

elif num == 2:
    ans = bin(random_num)[2:]
    answer = int(input(f"Convert the denary number {first_num} to binary"))

elif num == 3:
    rand_ans = hex(random_num)[2:]
    user_input = int(input(f"Convert the hexadecimal number {rand_ans} to denary"))
    ans = first_num

elif num == 4:
    ans = hex(random_num)[2:]
    answer = int(input(f"Convert the denary number {first_num} to hexadecimal"))



if user_input == ans:
        score += 1
        print("Correct!")
        print(f"You now have {score} points.")
else:
    score -= 1
    print(f"Incorrect, The correct answer was {ans}!")
    print(f"You now have {score} points.")

