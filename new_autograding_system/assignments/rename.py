from os import listdir, getcwd, rename


files = listdir()



for fn in files:

    

    new_fn = f"Python Challenges {fn.split('_')[0]}"
    
    rename(getcwd()+"/"+fn, getcwd()+"/"+new_fn)
        
            

