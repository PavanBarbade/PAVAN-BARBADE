import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

chrome_options = Options()
chrome_options.add_experimental_option(name="detach",value=True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://brightinfo.in")
driver.maximize_window()#above code is use for launching the browser
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="footer"]/div[2]/div/div/a').click()#use for button clicking
driver.find_element(By.ID,'username').send_keys("Bright@123")#inserting the name
driver.find_element(By.ID,'password').send_keys("pass123")
driver.find_element(By.XPATH,'/html/body/div[1]/div/form/div[3]/div/button').click()
