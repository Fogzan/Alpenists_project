import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time, sys
from selenium.webdriver.common.by import By

from authorization import authorization
from mountains import mountains
from climbers import climbers
from group import group
from climbing import climbing


def test_main():
   options = Options()
   options.add_argument('--headless')
   # options.add_argument('--no-sandbox')
   # options.add_argument('--disable-dev-shm-usage')
   driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

   driver.maximize_window()
   driver.implicitly_wait(5)
   
   driver.get("http://192.168.0.139:5000")

   result_authorization = authorization(driver=driver)
   assert result_authorization == True, "Ошибка в регистрации и авторизации."
   result_mountains = mountains(driver=driver)
   assert result_mountains == True, "Ошибка при добавлении горы."
   result_climbers = climbers(driver=driver)
   assert result_climbers == True, "Ошибка при добавлении альпиниста."
   result_group = group(driver=driver)
   assert result_group == True, "Ошибка при создании группы."
   result_climbing = climbing(driver=driver)
   assert result_climbing == True, "Ошибка при добавлении восхождения."

   driver.close()
   driver.quit()
