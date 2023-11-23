from selenium.webdriver.common.by import By
import uuid
from RandomWordGenerator import RandomWord

rw = RandomWord(max_word_size=10,
                constant_word_size=True,
                include_digits=False,
                include_special_chars=False)

def mountains(driver):
    if not create(driver=driver):
        return False
    if not edit(driver=driver):
        return False
    return True
    
def create(driver):
    try:
        driver.find_element(By.XPATH, "/html/body/header/nav/div/div/ul/li[1]/a").click()
        driver.find_element(By.XPATH, "/html/body/main/div/div/a").click()

        input_name = driver.find_element(By.ID, "name")
        input_height = driver.find_element(By.ID, "height")
        input_country = driver.find_element(By.ID, "country")
        input_district = driver.find_element(By.ID, "district")

        randomize = rw.generate()

        input_name.send_keys(randomize)
        input_height.send_keys(1000)
        input_country.send_keys(randomize)
        input_district.send_keys(randomize)

        driver.find_element(By.XPATH, "/html/body/main/div/form/div[5]/button").click()

        if "Гора успешно добавлена." in driver.find_element(By.XPATH, "/html/body/div/div").text :
            return True
        else:
            return False
    except:
        return False
    

def edit(driver):
    try:
        driver.find_element(By.XPATH, "/html/body/main/div/table/tbody/tr[1]/td[8]/a[2]").click()

        input_height = driver.find_element(By.ID, "height")

        input_height.clear()
        input_height.send_keys(19)

        driver.find_element(By.XPATH, "/html/body/main/div/form/div[5]/button").click()

        if "Гора успешно изменена." in driver.find_element(By.XPATH, "/html/body/div/div").text :
            return True
        else:
            return False
    except:
        return False
