from selenium.webdriver.common.by import By
import uuid
from RandomWordGenerator import RandomWord

rw = RandomWord(max_word_size=12,
                constant_word_size=True,
                include_digits=False,
                include_special_chars=False)

def group(driver):
    # result_create = create(driver=driver)
    # if not result_create[0]:
    #     return False
    # if not add_сlimbers(driver=driver, name_group=result_create[1]):
    #     return False
    return True

def create(driver):
    try:
        driver.find_element(By.XPATH, "/html/body/header/nav/div/div/ul/li[3]/a").click()
        driver.find_element(By.XPATH, "/html/body/main/div/div/a[1]").click()

        input_name = driver.find_element(By.ID, "name")

        randomize = rw.generate()

        input_name.send_keys(randomize)
        name_group = randomize

        driver.find_element(By.XPATH, "/html/body/main/div/form/div[2]/button").click()

        if "Группа успешно добавлена." in driver.find_element(By.XPATH, "/html/body/div/div").text :
            return (True, name_group)
        else:
            return (False, )
    except:
        return (False, )
    
def add_сlimbers(driver, name_group):
    try:
        count = 1
        while True: 
            if name_group in driver.find_element(By.XPATH, f"/html/body/main/div/table/tbody/tr[{count}]/td[2]").text:
                driver.find_element(By.XPATH, f"/html/body/main/div/table/tbody/tr[{count}]/td[4]/a").click()
                break
            count += 1

        driver.find_element(By.XPATH, "/html/body/main/div/form/div[1]/select").click()
        driver.find_element(By.XPATH, "/html/body/main/div/form/div[1]/select/option[2]").click()
        driver.find_element(By.XPATH, "/html/body/main/div/form/div[2]/button").click()

        if "Альпинист успешно добавлен к группе." in driver.find_element(By.XPATH, "/html/body/div/div").text :
            return True
        else:
            return False
    except:
        return False
