from helpers import get_students, load_module_from_path
from os import path
from pathlib import Path
from sys import modules, stdout
from unittest.mock import patch
from re import findall
from db import Database
from shutil import copy
from config import *

GRADED_ASSIGNMENTS = """001 Python Challenges I
002 Python Challenges II
003 Python Challenges III
004 Python Challenges IV
005 Python Challenges V
006 Python Challenges VI
007 Python Challenges VII
008 Python Challenges VIII
009 Python Challenges IX
010 Python Challenges X
015 Python Challenges XV
01b Python Challenges Ib
02b Python Challenges IIb
02c Python Challenges IIc
04b Python Challenges IVb
05b Python Challenges Vb""".splitlines()

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

                try:
                    module = load_module_from_path(stu_ass_path)
                except FileNotFoundError:
                    continue
                
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


##########################################

def generate_result_reports():

    with Database() as db:
        data = db.execute("""SELECT * FROM result
INNER JOIN assignment on result.assignment_id=assignment.assignment_id
INNER JOIN student on student.student_id = result.student_id
INNER JOIN class on student.class_id = class.class_id
ORDER BY result.student_id""")
    
    with open("results_template.html") as f:
        html_template = f.read()
    
    last_stu = None
    html_out = ""


    print(data)

    overall = []
    new_student = False
    for row in data:
       

        if row[7] != last_stu and last_stu is not None:     
            year_range = "23-25" # fix later
            stu_folder = f"Comp Sci {year_range} - {stu_name} [{class_name}]"
            new_file = path.join(STU_WORK_PATH, class_name, stu_folder, f"Python Challenges Results Report - {stu_name} [{class_name}].html")           
            print(overall)
            overall_score = str(round((sum(overall)/len(overall)) * 100, 2))
            print(overall_score)
            html_out = html_template.replace("<!-- result data here -->", html_out + f"\n</table>").replace("!score!", overall_score)

            with open(new_file, "w") as f:
                f.write(html_out)

            print(f"Just wrote {stu_name}'s results as", new_file)            

            new_student = True

        ass_id, _, passed, failed, _, ass_name, _, stu_name, _, _, class_name = row        

        if new_student:
            html_out = f"""{stu_name}</p>
            <p><strong>Class: </strong>{class_name}</p>
            <p><strong>Success: </strong>!score!% completion rate</p>
        <table>
            <colgroup>
                <col style="width: 20%;">
                <col style="width: 40%;">
                <col style="width: 20%;">
                <col style="width: 20%;">
            </colgroup>
            <tr>
                <th>Assignment ID</th>
                <th>Assignment Name</th>
                <th>Tests Passed</th>
                <th>Tests Failed</th>
            </tr>"""
            overall = []
            new_student = False

        

        try:
            overall.append(passed / (passed + failed))
            html_out += f"""
            <tr>
                <td>{ass_id}</td>
                <td>{ass_name}</td>
                <td>{passed}</td>
                <td>{failed}</td>"
            </tr>"""

        except ZeroDivisionError:
            pass

        
        
        
   
        last_stu = stu_name
            
        


if __name__ == "__main__":

    students = get_students()
    results = get_results(students)
    write_results(results)
    generate_result_reports()



                

print(result_data)

            
