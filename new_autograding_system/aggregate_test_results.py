from helpers import get_students
from os import path
from pathlib import Path
from importlib import import_module
from importlib.util import spec_from_file_location, module_from_spec
from sys import modules

GRADED_ASSIGNMENTS = """006 Python Challenges VI""".splitlines()



if __name__ == "__main__":

    students = get_students()


    for class_group, student_data in students.items():
        # go through each student
        for student_name, student_path in student_data:
            print("Assessing", student_name)
            suffix = f" - {student_name} [{class_group}]"
            for assignment in GRADED_ASSIGNMENTS:
                print("Assignment:", assignment)
                stu_ass_path = path.join(student_path, assignment+suffix, "tests.py")


                # Create a module name replacing spaces and special characters
                module_name = 'module_with_spaces'


                print(r"C:\Users\mrhallbkk\GitHub\replit_alternative\new_autograding_system\example_student_work\EXC1\Comp Sci 23-25 - jane_doe [EXC1]\006 Python Challenges VI - jane_doe [EXC1]")
                # Load the module
                spec = spec_from_file_location(module_name, stu_ass_path)
                module = module_from_spec(spec)
                modules[module_name] = module
                spec.loader.exec_module(module)
                module.run_tests()

                
                

            
