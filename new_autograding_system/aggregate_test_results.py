from helpers import get_students, load_module_from_path
from os import path
from pathlib import Path
from sys import modules, stdout
from unittest.mock import patch
from re import findall
from db import Database

GRADED_ASSIGNMENTS = """006 Python Challenges VI""".splitlines()

log = ""
result_data = {}



def record_output(*s):
    global log
    for item in s:
        log += item

def get_results(students: dict) -> dict:
    result_data = {}
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
                        module.run_tests(silent=True)
                print(log)
                passed = int(findall(r'(\d*)\stests\spassed', log)[-1])
                failed = int(findall(r'(\d*)\stests\sfailed', log)[-1])
                  
                this_result = {"student":student_name, "class":class_group, "failed":failed, "passed":passed}
                result_data[assignment].append(this_result)
                
    return result_data

def write_results(results):
    all_q = ""
    all_v = list()
    for assignment, data in results.items():
        for student in data:
            s, a, p, f = student["student"], assignment.split()[0], student["passed"], student["failed"]
            q = """INSERT INTO result
VALUES (?, (SELECT student_id FROM student WHERE name = ?), ?, ?)
ON CONFLICT DO UPDATE SET passed=?, failed=?;"""

            v = (a, s, p, f, p, f)

            with Database() as db:
                print(q, v)
                db.execute(q, v)



if __name__ == "__main__":

    students = get_students()
    results = get_results(students)
    write_results(results)




                

print(result_data)

            
