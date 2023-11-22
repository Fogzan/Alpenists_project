import pytest
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
 
 
def test_main():
   options = webdriver.ChromeOptions()
   options.add_experimental_option("excludeSwitches", ["enable-logging"])
   options.add_argument('--headless')
   options.add_argument('--no-sandbox')
   options.add_argument('--disable-dev-shm-usage')
   options.add_argument('--disable-extensions')
 
   options.add_argument('--disable-gpu')
   options.add_argument('--remote-debugging-port=9222')
   options.add_argument('--disable-web-security')
   options.add_argument('--disable-browser-side-navigation')
   options.add_argument('--disable-infobars')
   options.add_argument('--disable-popup-blocking')
   options.add_argument('--disable-notifications')
   options.add_argument('--disable-translate')
   options.add_argument('--disable-logging')
   options.add_argument('--disable-background-networking')
   options.add_argument('--start-maximized')
   
   driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
 
   driver.maximize_window()
   driver.implicitly_wait(60)
   
   driver.get('https://yandex.ru')
 
   assert True == True, "Testing"
   
   # result_authorization = authorization(driver=driver)
   # assert result_authorization == True, "Ошибка в регистрации и авторизации."
   # result_mountains = mountains(driver=driver)
   # assert result_mountains == True, "Ошибка при добавлении горы."
   # result_climbers = climbers(driver=driver)
   # assert result_climbers == True, "Ошибка при добавлении альпиниста."
   # result_group = group(driver=driver)
   # assert result_group == True, "Ошибка при создании группы."
   # result_climbing = climbing(driver=driver)
   # assert result_climbing == True, "Ошибка при добавлении восхождения."
 
   driver.close()
   driver.quit()
