from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from os import mkdir
from selenium.webdriver.common.by import By

def get_tests(driver):
    '''Create a directory corresponding with the assignment (if one doesn't already exist)
    Iterates through each I/O test and copies the test name, list of inputs and expected outputs
    Dumps these into an .io file in the assignment directory'''

    driver.switch_to.window(driver.window_handles[-1])
    ass_title = driver.find_element(By.CLASS_NAME, "css-6snj1q").get_attribute("innerHTML") + " test_cases"
    try:
        mkdir(ass_title)
    except:
        pass
    
    buttons = driver.find_elements(By.CLASS_NAME, "icon-container")[2::2]

    for button in buttons:
        
        button.click()        

        driver.find_element(By.CLASS_NAME, "css-1yo3rnk").click()
        driver.implicitly_wait(1)       

        test_name = driver.find_elements(By.CLASS_NAME, "jsx-3568970720")[-1].get_attribute("value")
        inputs = driver.find_elements(By.CLASS_NAME, "jsx-2488858501")[2].get_attribute("innerHTML")
        outputs = driver.find_elements(By.CLASS_NAME, "jsx-2488858501")[5].get_attribute("innerHTML")
        
        print(test_name, inputs, outputs)

        with open(f"{ass_title}/{test_name}.io", "w") as file:
            file.write('{"inputs":')
            file.write("["+",".join('"'+inp+'"' for inp in inputs.splitlines()) + "]")
            file.write(',\n"outputs":')
            file.write("["+",".join('"'+out+'"' for out in outputs.splitlines()) + "]")
            file.write("}")

        driver.find_element(By.CLASS_NAME, "css-1yo3rnk").send_keys(Keys.ESCAPE)

driver = webdriver.Chrome()

print("Please log into replit and navigate to your assignment page, then open TESTS.")
sleep(1)
print("Following this, call get_tests(driver) in the console to export your I/O tests.")
driver.get("https://replit.com/login")
