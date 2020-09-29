from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

url = "https://paytm.com/electricity-bill-payment"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(3)
wait = WebDriverWait(driver, 10)

state = "Madhya Pradesh"
board = "MP Madhya Kshetra Vidyut Vitran - Bhopal"
typeA = "Urban"
CusNo = "8048674000"

fill1 = driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[1]/div[1]/div/div[2]/div[2]/ul/li/div/div/input")
fill1.send_keys(state)
# time.sleep(1)
fill2 = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div[4]/div[1]/div[1]/div/div[2]/div[2]/ul/li[2]/div[1]/div/input")))
fill2.send_keys(board)
# time.sleep(1)
fill3 = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div[4]/div[1]/div[1]/div/div[2]/div[2]/ul/li[3]/div/div/input")))
fill3.send_keys(typeA)
# time.sleep(1)
fill4 = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div[4]/div[1]/div[1]/div/div[2]/div[2]/ul/li[4]/div[1]/input")))
fill4.send_keys(CusNo)
# time.sleep(1)

proceed = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div[4]/div[1]/div[1]/div/div[2]/div[5]/button")))
proceed.send_keys(Keys.ENTER)
#if you face error comment out time.sleep options in above script, this may help
print("Now Login and Pay Your Electricity Bill, Thank You")
