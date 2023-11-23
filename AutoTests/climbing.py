from selenium.webdriver.common.by import By
import uuid
from RandomWordGenerator import RandomWord

rw = RandomWord(max_word_size=10,
                constant_word_size=True,
                include_digits=False,
                include_special_chars=False)

def climbing(driver):
    # if not create(driver=driver):
    #     return False
    # if not create_2(driver=driver):
    #   return False
    return True
    
def create(driver):
    try:
        driver.find_element(By.XPATH, "/html/body/header/nav/div/div/ul/li[4]/a").click()
        driver.find_element(By.XPATH, "/html/body/main/div/div/a[1]").click()

        driver.find_element(By.XPATH, "/html/body/main/div/form/div[1]/select").click()
        driver.find_element(By.XPATH, "/html/body/main/div/form/div[1]/select/option[2]").click()

        driver.find_element(By.XPATH, "/html/body/main/div/form/div[2]/select").click()
        driver.find_element(By.XPATH, "/html/body/main/div/form/div[2]/select/option[2]").click()

        input_dateStart = driver.find_element(By.ID, "dateStart")
        input_dateEnd = driver.find_element(By.ID, "dateEnd")

        input_dateStart.send_keys("01.11.200323:30")
        input_dateEnd.send_keys("01.12.200322:30")

        driver.find_element(By.XPATH, "/html/body/main/div/form/div[5]/button").click()

        if "Восхождение успешно добавлено." in driver.find_element(By.XPATH, "/html/body/div/div").text :
            return True
        else:
            return False
    except:
        return False
    
def create_2(driver):
    try:
        driver.find_element(By.XPATH, "/html/body/main/div/div/a[2]").click()

        input_name = driver.find_element(By.ID, "name")

        randomize = rw.generate()

        input_name.send_keys(randomize)

        driver.find_element(By.XPATH, "/html/body/main/div/form/div[2]/select").click()
        driver.find_element(By.XPATH, "/html/body/main/div/form/div[2]/select/option[2]").click()

        input_dateStart = driver.find_element(By.ID, "dateStart")
        input_dateEnd = driver.find_element(By.ID, "dateEnd")

        input_dateStart.send_keys("01.11.200323:30")
        input_dateEnd.send_keys("01.12.200322:30")

        driver.find_element(By.XPATH, "/html/body/main/div/form/div[5]/button").click()

        if "Восхождение успешно добавлено." in driver.find_element(By.XPATH, "/html/body/div/div").text :
            return True
        else:
            return False
    except:
        return False
    
