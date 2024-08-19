from os import getcwd, listdir, path, mkdir
from re import match, search
from datetime import datetime
from helpers import get_students, hide_file
from shutil import copy
from config import *

def choose_assignments(options: list[str]) -> list[int]:
    chosen = options

    all_ass = input("Redistribute all assignments? Enter any key: ")
    if not len(all_ass):
        chosen = input("OK. Enter comma separated list of assignment numbers: ")
        
        for choice in chosen.split(","):
            if not choice.isdigit() or int(choice)-1 not in options:
                print(choice.center(10), "<- invalid choice")
                return None

    chosen = [int(choice)-1 for choice in chosen.split(",")]


    return chosen

###############################

def get_assignments() -> list[str]:

    # iterate assignments folder
    # display menu
    count = 1
    options = []
    for assignment in sorted(listdir(ASS_PATH)):
        this_path = path.join(getcwd(), ASS_PATH, assignment)
        if not path.isdir(this_path): continue
        print(f"{str(count).center(3)}. {assignment}")
        count += 1
        options.append(assignment)

    # validate selection
    chosen = None
    while chosen is None:
        chosen = choose_assignments(list(range(len(options))))
    print("OK distributing...")
    for choice in chosen:
        print(options[int(choice)])
    # return paths
    return [path.join(ASS_PATH, options[i]) for i in chosen]



###############################

def explore_assignment_directory(ass_path: str, stu_path: str):

    for fn in listdir(ass_path):
        if fn in IGNORE:    continue
        
        potential_path = path.join(ass_path, fn)
        print("Check potential path", potential_path)
        if path.isdir(potential_path):
            ass_path = potential_path
            stu_path = path.join(stu_path, fn)
            create_dir(stu_path)
            explore_assignment_directory(ass_path, stu_path)
        else:
            redistribute_file(ass_path, stu_path, fn)

###############################

def create_dir(this_dir):
    if not path.exists(this_dir):
        mkdir(this_dir)

###############################

def create_backup(old_file):
    stamp = datetime.now().strftime("%Y.%m.%d.%H.%M.%S")                    
    chunks = path.split(old_file)
    
    backup = path.join(*chunks[:1])
    backup_dir = path.join(backup, "backup")
    create_dir(backup_dir)
    hide_file(backup_dir)
                       
    backup = path.join(backup, "backup", f"{stamp}_{chunks[-1]}")
    copy(old_file, backup)
    hide_file(backup)

###############################

def redistribute_file(ass_path: str, stu_path: str, fn: str):

    old_file = path.join(stu_path, fn)
    new_file = path.join(ass_path, fn)

    check = True
    print("Checking if", old_file, "exists")
    
    if path.exists(old_file):        
        if path.getmtime(new_file) > path.getmtime(old_file) or old_file.endswith(".py"):
            check = bool(input(f"Replace {old_file} - are you sure? "))
            if check:
                create_backup(old_file)         
    else:
        print("File not found, writing new file")
    if check:        
        print("Copied the file.")
        copy(new_file, old_file)
        

###############################

def distribute(ass_paths: list[str], students: dict):
    ""
    # go through each class
    for class_group, student_data in students.items():
        # go through each student
        for student_name, student_path, _ in student_data:
            # go through each assignment
            for assignment_path in ass_paths:
                ass_found = False
                print("Processing", assignment_path)
                suffix = f" - {student_name} [{class_group}]"
                new_ass_path = path.join(*path.split(assignment_path)[1:]) + suffix
                this_students_assignment = path.join(student_path, new_ass_path)
                create_dir(this_students_assignment)
                
                explore_assignment_directory(assignment_path, this_students_assignment)

                # if this file has tests, distribute the test runner and test hash
                if path.exists(path.join(this_students_assignment, "test_cases")):
                    copy(path.join(getcwd(), "tests.py"), path.join(this_students_assignment, "tests.py"))
                    copy(path.join(getcwd(), "test_hash.py"), path.join(this_students_assignment, "test_cases", "test_hash.py"))
                    print("Redistributed unit tests")

###############################                    
                  

if __name__ == "__main__":

    ass_paths = get_assignments()
    students = get_students()
    distribute(ass_paths, students)
