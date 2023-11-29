from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import mkdir
from selenium.webdriver.common.by import By
import json

def add_tests(driver):
    '''Create a directory corresponding with the assignment (if one doesn't already exist)
    Iterates through each I/O test and copies the test name, list of inputs and expected outputs
    Dumps these into an .io file in the assignment directory'''

    driver.switch_to.window(driver.window_handles[-1])

    for fn in listdir():
        if fn.endswith("io"):
            with open(fn) as f:
                data = json.load(f)
                driver.find_element(By.CLASS_NAME, "jsx-1681493817").click() # create test

                test_name = driver.find_elements(By.CLASS_NAME, "jsx-3568970720")[-1]
                test_name.send_keys(fn)
                inputs = driver.find_elements(By.CLASS_NAME, "jsx-2488858501")[2]
                inputs.send_keys("\n".join(data["inputs"]))
                outputs = driver.find_elements(By.CLASS_NAME, "jsx-2488858501")[5]
                outputs.send_keys_keys("\n".join(data["outputs"]))

                driver.find_element(By.CLASS_NAME, "jsx-2010878951").click() # save

        

driver = webdriver.Chrome()

print("Please log into replit and navigate to your assignment page, then open TESTS.")
sleep(1)
print("Following this, call add_tests(driver) in the console to input your I/O tests.")
driver.get("https://replit.com/login")
