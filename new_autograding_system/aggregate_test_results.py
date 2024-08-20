from helpers import get_students, load_module_from_path
from os import path
from pathlib import Path
from sys import modules, stdout
from unittest.mock import patch
from re import findall

GRADED_ASSIGNMENTS = """006 Python Challenges VI""".splitlines()

log = ""
result_data = {}



def record_output(*s):
    global log
    for item in s:
        log += item



if __name__ == "__main__":

    students = get_students()


    for class_group, student_data in students.items():
        # go through each student
        for student_name, student_path in student_data:
            print("Assessing", student_name)
            suffix = f" - {student_name} [{class_group}]"
            for assignment in GRADED_ASSIGNMENTS:
                if assignment not in result_data:
                    result_data[assignment] = []
                print("Assignment:", assignment)
                
                stu_ass_path = path.join(student_path, assignment+suffix, "tests.py")
                
                module = load_module_from_path(stu_ass_path)
                
                with patch("builtins.input", side_effect=lambda x: ""):
                    with patch("sys.stdout.write", side_effect=record_output):
                        module.run_tests(silent=False)
                print(log)
                input()
                passed = int(findall(r'(\d*)\stests\spassed', log)[-1])
                failed = int(findall(r'(\d*)\stests\sfailed', log)[-1])
                  
                this_result = {"student":student_name, "class":class_group, "failed":failed, "passed":passed}
                result_data[assignment].append(this_result)



print(result_data)

            
