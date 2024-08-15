from os import listdir, getcwd, rename


files = listdir()

name1 = input("Enter name to replace: ")
name2 = input("Enter name to replace with: ")

for fn in files:
    
    rename(getcwd()+"/"+fn, getcwd()+"/"+fn.replace(name1, name2))
        
            

