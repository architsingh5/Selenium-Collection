from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import xlrd
import pathlib
import time


print("Wait for Some time, Your Cart is loading up...")

#code to read from excel file
loc = str(pathlib.Path(__file__).parent.absolute()) + '/medicinelist.xlsx'

wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0)

list = []

for i in range(2,sheet.nrows):
    list.append(sheet.cell_value(i, 0))

#driver starts
url = "https://www.netmeds.com"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url)
time.sleep(3)

wait = WebDriverWait(driver, 10)

#if you are some facing issues, try to increase sleep times, this may help
for med_name in list:
    search_box = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/header/div/div/div[2]/div/div[2]/form/div/div/input")))
    search_box.send_keys(med_name,Keys.ENTER)
    time.sleep(2)
    add = driver.find_elements_by_class_name("toCart")[0]
    add.send_keys(Keys.ENTER)
    time.sleep(1)

time.sleep(2)
driver.get("https://www.netmeds.com/checkout/cart")
pin_input = wait.until(EC.presence_of_element_located((By.ID, 'delivering_to')))
pin_input.clear()
pin_input.send_keys("462003")

print("Your Cart is complete, now click on Proceed option to continue...Thanks")
