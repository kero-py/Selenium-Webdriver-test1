from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.get("https://www.selenium.dev/")
time.sleep(3)
driver.close()
 