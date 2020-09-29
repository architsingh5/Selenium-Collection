from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pathlib

driver = webdriver.Chrome()
driver.maximize_window()

url = "https://www.indiapost.gov.in/_layouts/15/dop.portal.tracking/trackconsignment.aspx"
driver.get(url)

# Change the consignment no. to your Speed Post's Consignment no. in consignmentNo.txt File
# 
f = open(str(pathlib.Path(__file__).parent.absolute()) + '/consignmentNo.txt')
s1 = f.read()

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, 'ctl00_PlaceHolderMain_ucNewLegacyControl_txtOrignlPgTranNo')))
element.send_keys(s1)

print("\nSolve the captcha and Click on Search, ThankYou")

