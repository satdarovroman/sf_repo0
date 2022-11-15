#python -m pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome("D:\skillfactory\repo3\repo3\chromedriver.exe")
driver.get("https://google.com")
driver.find_element(By.XPATH, "//input[@title=\"Поиск\"]").send_keys('Skillfactory' + Keys.RETURN)

sleep(2)
driver.save_screenshot('sf.png')

driver.quit()

