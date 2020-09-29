from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = None
url = "https://www.covid19india.org/"

def start():
    global driver
    driver = webdriver.Chrome() 
    driver.maximize_window()


def state_statistics():
    state = input("Enter the name of the State\n")
    state += " "
    start()
    driver.get(url)
    # increase the below time if your connection speed is low
    time.sleep(3)
    element = driver.find_element_by_xpath("/html/body/div/div/div[3]/div[1]/div[1]/div[1]/div[2]/input")
    element.send_keys(state)
    time.sleep(2)
    element.send_keys(Keys.BACKSPACE)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME,'result')))
    result = driver.find_elements_by_class_name("result")[0]
    result.click()


if __name__ == "__main__":    
    print("Enter the number from the list")
    print("1. All India Statistics")
    print("2. Specific State Statistics")

    a=int(input())

    if(a==1):
        start()
        driver.get(url)

    elif(a==2):
        state_statistics()
