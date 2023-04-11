from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('http://127.0.0.1:5000/')
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/div/div/p/a').click()
username = "Testing@tester.co.uk"
password = "password123"
driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(username)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
driver.find_element(By.XPATH, '//*[@id="submit"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[2]/header/nav/ul/li[3]/a').click()
time.sleep(5)
driver.close()
 
