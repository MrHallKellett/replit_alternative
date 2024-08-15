from os import listdir
from json import loads
from unittest.mock import patch
from sys import stdout
from importlib import reload
from time import sleep

RED = (255, 0, 0)
GREEN = (0, 255, 0)
PATH = "test_cases/"


def print_in_colour(x, end, sep, colour):
    set_colour(colour)
    print(" ".join(str(i) for i in x))
    reset_colour()

def print_red(*x, end="\n", sep=" "):
    print_in_colour(x, end=end, sep=sep, colour=RED)

def print_green(*x, end="\n", sep=" "):
    print_in_colour(x, end=end, sep=sep, colour=GREEN)

def set_colour(colour):
    stdout.write(f"\033[38;2;{colour[0]};{colour[1]};{colour[2]}m")
    
def reset_colour():
    stdout.write("\033[0m")


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
            try:
                with open(PATH+test, encoding="unicode-escape") as f:
                    tests[test] = loads(f.read())
            except Exception as e:
                print_red(f"Skipping {test} as : {e}")
                continue
        return tests

    def __init__(self):
        result = ""
        test_stats = [0, 0]
        first = True
		
        tests = self.load_tests()
		

        for test_name, test_data in tests.items():
            self.input_queue = test_data["inputs"]
            self.printed = "INPUT/OUTPUT LOG:\n"
            s = f"RUNNING TEST: {test_name}..."
            print(len(s)*"-")
            print(s)    
            print(len(s)*"-")
            
            try:
                with patch("builtins.input", side_effect=self.mock_input):
                    with patch("builtins.print", side_effect=self.log_print):
                        if first:
                            import main
                            first = False
                        else:       
                            reload(main)

            except Exception as e:                
                print_red(e)                
                test_stats[1] += 1
                continue
                    
            self.printed = self.printed.replace("\n\n", "\n")      

            printed_copy = self.printed

            for i, line in enumerate(test_data["outputs"]):        
                print(f"expected output {i+1}...", end=" ")
                if line in self.printed:                                
                    print_green("FOUND", line)      
                    self.printed = self.printed.replace(line, "", 1)                              
                else:                                
                    print_red("NOT FOUND\n")
                    print_red("\tCould not find... ")                                
                    print("\t\t'"+line+"'")         
                    print_red("\tin ...")  
                    for line in printed_copy.splitlines():                      
                        print("\t\t"+line)
                    test_stats[1] += 1
                    
            else:
                test_stats[0] += 1
        
        print_green(test_stats[0], "tests passed!")        
        print_red(test_stats[1], "tests failed!")


if __name__ == "__main__":
    TestRunner()
    print()
    input("Press any key to quit")
