from os import getcwd, listdir, path

ASS_PATH = "/assignments/"
STU_WORK_PATH = "/example_student_work/"


def choose_assignments(options):
    chosen = options
    all_ass = input("Distribute all assignments? Enter any key: ")
    if not  len(all_ass):
        chosen = input("OK. Enter comma separated list of assignment numbers: ")
        
        for choice in chosen.split(","):
            if not choice.isdigit() or int(choice) not in options:
                print(choice.center(10), "<- invalid choice")
                return None

        chosen = [int(choice) for choice in chosen.split(",")]

    return chosen

###############################

def get_assignments() -> list[str]:

    # iterate assignments folder
    # display menu
    count = 1
    options = []
    for assignment in sorted(listdir(ASS_PATH)):
        if not path.isdir(getcwd()+"/"+ASS_PATH+"/"+assignment): continue
        print(f"{str(count).center(3)}. {assignment}")
        count += 1
        options.append(assignment)

    # validate selection
    chosen = choose_assignments(list(range(len(options))))
        
    # return paths
    return [options[i-1] for i in chosen]


def get_students() -> list[str]:

    # iterate student work folder
    for class_group in sorted(listdir(STU_WORK_PATH)):
    # return paths
    ""

def distribute(ass_paths: list[str], students: list[str]):
    ""
    # iterate students

        # iterate ass_paths

            # ass files exist?

                # newer? replace. ignore main.py unless flag

            # else

                # write

            









if __name__ == "__main__":

    ass_paths = get_assignments()
    students = get_students()
    distribute(ass_paths, students)
