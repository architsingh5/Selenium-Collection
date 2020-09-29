from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

url = "https://formbuddy5.netlify.app/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(3)

name = "Archit Singh"
sch = "191112472"
email = "architsingh5@gmail.com"

namef = driver.find_element_by_xpath("/html/body/section/div/form/div[1]/input")
namef.send_keys(name)
schf = driver.find_element_by_xpath("/html/body/section/div/form/div[2]/input")
schf.send_keys(sch)
emailf = driver.find_element_by_xpath("/html/body/section/div/form/div[3]/input")
emailf.send_keys(email)

time.sleep(2)

btn = driver.find_element_by_xpath("/html/body/section/div/form/button")
btn.send_keys(Keys.ENTER)




