from selenium.webdriver.common.by import By
import uuid
from RandomWordGenerator import RandomWord

rw = RandomWord(max_word_size=6,
                constant_word_size=True,
                include_digits=False,
                include_special_chars=False)

def climbers(driver):
    # if not create(driver=driver):
    #     return False
    return True

def create(driver):
    try:
        driver.find_element(By.XPATH, "/html/body/header/nav/div/div/ul/li[2]/a").click()
        driver.find_element(By.XPATH, "/html/body/main/div/div/a[1]").click()

        input_fio = driver.find_element(By.ID, "fio")
        input_address = driver.find_element(By.ID, "address")

        randomize = rw.generate()

        input_fio.send_keys(randomize + " " + randomize + " " + randomize)
        input_address.send_keys(randomize + randomize + randomize)

        driver.find_element(By.XPATH, "/html/body/main/div/form/div[3]/button").click()

        if "Альпинист успешно добавлен." in driver.find_element(By.XPATH, "/html/body/div/div").text :
            return True
        else:
            return False
    except:
        return False
