from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time, sys
from selenium.webdriver.common.by import By

from authorization import authorization
from mountains import mountains
from climbers import climbers
from group import group
from climbing import climbing

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.maximize_window()
driver.implicitly_wait(5)

driver.get("http://192.168.0.139:5000")
# time.sleep(5)

result_authorization = authorization(driver=driver)
print(result_authorization)
if not result_authorization:
   sys.exit("Ошибка в регистрации и авторизации")
result_mountains = mountains(driver=driver)
print(result_mountains)
if not result_mountains:
   sys.exit("Ошибка при добавлении горы")
result_climbers = climbers(driver=driver)
print(result_climbers)
if not result_climbers:
   sys.exit("Ошибка при добавлении альпиниста")
result_group = group(driver=driver)
print(result_group)
if not result_group:
   sys.exit("Ошибка при создании группы")
result_climbing = climbing(driver=driver)
print(result_climbing)
if not result_climbing:
   sys.exit("Ошибка при добавлении восхождения")