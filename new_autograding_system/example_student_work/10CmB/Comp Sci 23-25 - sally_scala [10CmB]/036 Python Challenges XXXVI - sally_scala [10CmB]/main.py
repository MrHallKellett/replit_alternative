def Exercise1():
    colours = {'red','orange','yellow','pink','violet'}
    return colours

def Exercise2():
    bathroom = ['green','turquoise','blue','white', 'gray']
    livingroom = ['red', 'pink', 'cream','brown','white']
    kitchen = ['red','orange','yellow','pink','violet']
    house = [bathroom, livingroom, kitchen]
    return house
    
def Exercise3(x):
    print("The first colour of the third room is " + x[2][0])
    print("The last colour of the last room is " + x[-1][-1])
    print("The third letter of the second colour of the first room is " + x[0][1][2])
    
def Exercise4(house):
    for room in house:
        for color in room:
            print(color, end=' ')
        print()

        




e = Exercise4(Exercise2())
print(e)



