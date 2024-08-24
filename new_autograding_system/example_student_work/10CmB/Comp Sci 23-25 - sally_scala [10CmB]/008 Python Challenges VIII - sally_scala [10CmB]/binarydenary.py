from random import randint
points = 0

while points != 10: 
    random_number = randint(0,10)
    option = randint(1,6)
    binary = bin(random_number)[2:]
    hexadecimal = hex(random_number)[2:]
    denary = random_number

    if option == 1:
        correct = binary
        print(correct)        
        answer = input('Convert the denary number '+str(random_number)+' into binary')

    elif option == 2:
        correct = hexadecimal
        print(correct)        
        answer = input('Convert the denary number '+str(random_number)+' into hexadecimal')
    
    elif option == 3:
        correct = denary
        print(correct)        
        answer = input('Convert the binary number '+str(binary)+' into denary')


    elif option == 4:
        correct = hexadecimal
        print(correct)
        answer = input('Convert the binary number '+str(binary)+' into hexadecimal')


    elif option == 5:
        correct = denary
        print(correct)
        answer = input('Convert the hexadecimal number '+str(hexadecimal)+' into denary')


    elif option == 6:
        correct = binary
        print(correct)
        answer = input('Convert the hexadecimal number '+str(hexadecimal)+' into binary')
        correct = binary 

    if answer == correct:
        points += 1
        print("you have "+str(points)+" point")
    else: 
        points -= 1
        print("inncorect " + str(points)+" point")
