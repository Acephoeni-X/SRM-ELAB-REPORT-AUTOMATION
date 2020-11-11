from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

username = ""
password = ""

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://care.srmist.edu.in/srmncrds/login')
username = "RA1911003030293"
password = "Rishi2002"

driver.find_element_by_xpath('//*[@id="mat-input-0"]').send_keys(username)
driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys(password)

driver.find_element_by_xpath('/html/body/app-root/div/app-login/div/mat-card/div[2]/form/button').click()
wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-student-home/div/mat-card/div/div/app-student-home-card/mat-card/p')))
element.click()

time.sleep(2)
driver.get('https://care.srmist.edu.in/srmncrds/student/solve/1411111')