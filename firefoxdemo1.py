from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get('http://127.0.0.1:5000/')
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/p/a').click()
username = "Testing@tester.co.uk"
password = "password123"
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(username)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="submit"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/header/nav/ul/li[3]/a').click()
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div[2]/header/nav/ul/li[4]/a').click()
time.sleep(3)
driver.close()