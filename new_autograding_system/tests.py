from os import listdir, path
from unicodedata import east_asian_width
from json import loads
from unittest.mock import patch
from sys import stdout
from importlib import reload
from time import sleep

INDENT = "  "
INDENT_2 = INDENT * 2
RED = (255, 0, 0)
GREEN = (0, 255, 0)
PATH = path.join(path.dirname(path.realpath(__file__)), "test_cases")

display = True
hidden_feedback = [""]

def print_if_logging(*x, end="\n", sep=" "):
    
    to_print = " ".join(str(i) for i in x)

    if display:
        stdout.write(to_print + end)
        
    else:
        hidden_feedback[-1] += to_print
        if end == "\n":
            hidden_feedback.append("")
        else:
            hidden_feedback[-1] += end

def print_in_colour(*x, end="\n", sep=" ", colour=None):    
    if colour:
        set_colour(colour)
    print_if_logging(*x, end=end, sep=sep)
    reset_colour()

def print_red(*x, end="\n", sep=" "):
    print_in_colour(*x, end=end, sep=sep, colour=RED)

def print_green(*x, end="\n", sep=" "):    
    print_in_colour(*x, end=end, sep=sep, colour=GREEN)

def print_standard(*x, end="\n", sep=" ", colour=None):
    reset_colour()
    print_if_logging(*x, end=end, sep=sep)

def set_colour(colour):
    if colour:
        colour_code = f"\033[38;2;{colour[0]};{colour[1]};{colour[2]}m"
    else:
        colour_code = "\033[0m"
    if display:
        stdout.write(colour_code)
    else:
        hidden_feedback[-1] += colour_code

def print_with_border(s, colour=None, top=True):     

    def visual_length(text):
        return sum(2 if east_asian_width(char) in 'WF' else 1 for char in text)

    p = print_standard if not colour else print_in_colour
    
    
    border_length = visual_length(s)
    
    print_standard()
    if top:
        print_standard(border_length*"-")
    p(s, colour=colour)
    print_standard(border_length*"-")
    
def reset_colour():
    set_colour(None)

class TestRunner:

    def log_print(self, *string, end="\n", sep=" "):
        
        self.printed += sep.join(str(s) for s in string)   
        self.printed += end

    def mock_input(self, prompt=""):

        self.log_print(prompt)
        try:
            this_inp = self.input_queue.pop(0)
            self.log_print(this_inp)
            return this_inp
        except IndexError:
            return ""
                
    def load_tests(self):

        tests = {}
        for test in sorted(listdir(PATH)):
            if not test.endswith(".io"): continue
            this_test_path = path.join(PATH, test)
            try:
                with open(this_test_path, encoding="unicode-escape") as f:
                    tests[test] = loads(f.read())
            except Exception as e:
                print_red(f"Skipping {test} as : {e}")
                continue
        return tests

    def __init__(self):
        global display
        result = ""
        test_stats = [0, 0]
        first = True
		
        tests = self.load_tests()

        def display_inputs(inputs):
            print_red(INDENT+"after providing the inputs ...")
            for line in inputs:
                print_standard(INDENT_2+line)

		

        for test_name, test_data in tests.items():
            self.input_queue = list(test_data["inputs"])
            self.printed = "INPUT/OUTPUT LOG:\n"
            s = f"RUNNING TEST: {test_name}..."
            
            print_with_border(s)
            
            try:
                with patch("builtins.input", side_effect=self.mock_input):
                    with patch("builtins.print", side_effect=self.log_print):
                        if first:
                            import main
                            first = False
                        else:       
                            reload(main)

            except Exception as e:                
                print_standard("could not complete test suite due to error:")
                print_red(e)                
                test_stats[1] += 1
                print_standard()
                display_inputs(test_data["inputs"])

                print_standard("\ncheck carefully for infinite loops / too many iterations")
                print_red("\n❌ TEST FAILED")
                    
                
                display = False
                continue
                    
            self.printed = self.printed.replace("\n\n", "\n")      
            ignore = test_data.get("ignore")
            print_test = self.printed

            if ignore:
                for item_to_ignore in ignore:
                    print_test = print_test.replace(item_to_ignore, "")

            for i, line in enumerate(test_data["outputs"]):        
                print_standard(f"expected output {i+1}...", end=" ")
                line_test = line

                if ignore:
                    for item_to_ignore in ignore:
                    
                        line_test = line_test.replace(item_to_ignore, "")

                if line_test in print_test:
                    print_green("FOUND")      
                    print_test = print_test.replace(line, "", 1)                              
                else:                                
                    print_red("NOT FOUND\n")
                    print_red(INDENT+"Could not find... ")                                
                    print_standard(INDENT_2+"'"+line+"'")         
                    print_red(INDENT+"in ...")  
                    for line in self.printed.splitlines():                      
                        print_standard(INDENT_2+line)
                    test_stats[1] += 1
                    
                    display_inputs(test_data["inputs"])

                    
                    print_red("\n❌ TEST FAILED")
                    
                    
                    display = False

                    
                    
            if display:
                
                print_green("\n✅ TEST PASSED")
                
                
                test_stats[0] += 1
        
        display = True
        s = "TEST RESULT SUMMARY:"        
        print_with_border(s)        
        print_green(test_stats[0], "tests passed!")        
        print_red(test_stats[1], "tests failed!")

        self.stats = test_stats


if __name__ == "__main__":
    this_test = TestRunner()
    print()
    exit_prompt = "Press any key to quit\n"
    if this_test.stats[1] > 0:
        exit_prompt = "Press A to view all test results, press any other key to quit\n"

    x = input(exit_prompt)
    if x.lower().strip() == "a":
        for line in hidden_feedback:
            print(line)
