from os import listdir, getcwd, path, rmdir, mkdir
from shutil import copy, copytree
from re import search

root = getcwd()

assignment_root = "C:\\Users\\mrhallbkk\\OneDrive - Kellett School\\Teaching\\problem_resources"

def distribute_tests(new_path, folder_name):
        try:
                assignment = folder_name.split(" ")[2]
        except IndexError:
                print(f"Error finding ass_code from {folder_name}")
                return False
        
        copy(root+"/tests.py", new_path+"/tests.py")
        print(f"Distributed test runner to {new_path}")
        try:
                mkdir(new_path+"/test_cases")
        except Exception as e:
                print(e)
                pass
        new_path += "/test_cases"
        
        

        for fn in listdir(assignment_root):
                ass_code = fn.split("_")[0]
                if ass_code == assignment:
                        assignment = fn
                        break
        else:
                print("Error finding", ass_code)
                input()
                
        
        this_ass_tests = assignment_root+"/"+assignment+"/test_cases"
        try:
                copytree(this_ass_tests,
                         new_path, dirs_exist_ok=True)
        except FileNotFoundError as e:
                print(e)
                print(f"Couldn't find test cases for {assignment}")
                
        print(f"Successfully copied {this_ass_tests} to {new_path}")

        return True

def walk(this_path):
        print("Traversing", this_path)
        for fn in listdir(this_path):
                new_path = this_path+"/"+fn
                if path.isdir(new_path):                 
                        if fn.startswith("Python Challenges"):                        
                                success = distribute_tests(new_path, fn)
                                if success:     continue
                        
                        walk(new_path)
                        
                                
                                

if __name__ == "__main__":
        walk(getcwd())


