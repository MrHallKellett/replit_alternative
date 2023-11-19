from os import listdir
from json import loads
from unittest.mock import patch
import sys

RED = (255, 0, 0)
GREEN = (0, 255, 0)
PATH = "test_cases/"    

def set_colour(colour):
    sys.stdout.write(f"\033[38;2;{colour[0]};{colour[1]};{colour[2]}m")
    
def reset_colour():
    sys.stdout.write("\033[0m")

def log_print(*string, end="", sep=" "):
    global printed
    for s in string:
        printed += s + sep
    printed += end

def mock_input(prompt=""):
    log_print(prompt)
    return input_queue.pop(0)
            
tests = {}
for test in listdir(PATH):
    with open(PATH+test) as f:
        tests[test] = loads(f.read())

result = ""

for test_name, test_data in tests.items():
    printed = ""
    input_queue = test_data["inputs"]
    with patch("builtins.input", side_effect=mock_input):
        with patch("builtins.print", side_effect=log_print):            
            import main
            ## not working yet
            
    print(f"RUNNING TEST: {test_name}")

    for line in test_data["outputs"]:        
        if line in printed:
            set_colour(GREEN)
            print("PASSED:")
        else:
            set_colour(RED)
            print("FAILED:")
        reset_colour()

        print(line)
            

    
