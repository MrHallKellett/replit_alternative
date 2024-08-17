from os import getcwd, listdir, path, mkdir
from re import match, search
from datetime import datetime
from helpers import hide_file
from shutil import copy

ASS_PATH = "assignments"
STU_WORK_PATH = "example_student_work"
IGNORE = """input-output matching
solutions""".splitlines()
BACK_UP = True

def choose_assignments(options: list[str]) -> list[int]:
    chosen = options
    all_ass = input("Redistribute all assignments? Enter any key: ")
    if not len(all_ass):
        chosen = input("OK. Enter comma separated list of assignment numbers: ")
        
        for choice in chosen.split(","):
            if not choice.isdigit() or int(choice) not in options:
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

def get_students() -> list[str]:
    students = {}
    # iterate student work folder
    for class_group in sorted(listdir(STU_WORK_PATH)):
        print("Found class", class_group)
        this_path = path.join(STU_WORK_PATH, class_group)
        students[class_group] = []
        for student in sorted(listdir(this_path)):
            name = " ".join(student.split(" ")[4:][:-1])
            print("\tFound student", name)
            students[class_group].append((name, path.join(STU_WORK_PATH, class_group, student)))
    return students

###############################

def explore_assignment_directory(ass_path: str, stu_path: str):

    for fn in listdir(ass_path):
        if fn in IGNORE:    continue
        
        potential_path = path.join(ass_path, fn)
        if path.isdir(potential_path):
            ass_path = potential_path
            stu_path = path.join(stu_path, fn)
            explore_assignment_directory(ass_path, stu_path)
        else:
            redistribute_file(ass_path, stu_path, fn)

###############################

def create_backup(old_file):
    stamp = datetime.now().strftime("%Y.%m.%d.%H.%M.%S")                    
    chunks = path.split(old_file)
    
    backup = path.join(*chunks[:1])
    backup_dir = path.join(backup, "backup")
    if not path.exists(backup_dir):
        mkdir(backup_dir)
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
        if path.getmtime(new_file) > path.getmtime(old_file):
            if old_file.endswith(".py"):
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
        for student_name, student_path in student_data:
            # go through each assignment
            for assignment_path in ass_paths:
                ass_found = False
                print("Processing", assignment_path)
                suffix = f" - {student_name} [{class_group}]"
                new_ass_path = path.join(*path.split(assignment_path)[1:]) + suffix
                this_students_assignment = path.join(student_path, new_ass_path)


                explore_assignment_directory(assignment_path, this_students_assignment)

###############################                    
                  

if __name__ == "__main__":

    ass_paths = get_assignments()
    students = get_students()
    distribute(ass_paths, students)
