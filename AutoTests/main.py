from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time, sys
from selenium.webdriver.common.by import By

from authorization import authorization
from mountains import mountains
from climbers import climbers
from group import group

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("http://192.168.0.139:5000")
# time.sleep(5)

result_authorization = authorization(driver=driver)
result_mountains = mountains(driver=driver)
result_climbers = climbers(driver=driver)
result_group = group(driver=driver)
print(result_authorization)
print(result_mountains)
print(result_climbers)
print(result_group)


if not result_authorization:
   sys.exit("some error message")

   
