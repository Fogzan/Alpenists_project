from selenium.webdriver.common.by import By
import uuid

def authorization(driver):
    result_create = create(driver=driver)
    if not result_create[0]:
        return False
    result_login = login(driver, data=result_create[1])
    if not result_login:
        return False
    
    return True

def create(driver):
    try:
        driver.get("http://192.168.0.107:5000/auth/new_user")
        input_username = driver.find_element(By.XPATH, "/html/body/main/div/form/div[1]/input")
        input_password = driver.find_element(By.XPATH, "/html/body/main/div/form/div[2]/input")
        input_password_replay = driver.find_element(By.XPATH, "/html/body/main/div/form/div[3]/input")
        randomize = str(uuid.uuid4())
        login = str(randomize)
        password = str(randomize)
        data = {
            'login': login,
            'password': password,
        }
        print(data)
        input_username.send_keys(login)
        input_password.send_keys(password)
        input_password_replay.send_keys(password)
        driver.find_element(By.XPATH, "/html/body/main/div/form/button").click()
        if "Пользователь успешно добавлен." in driver.find_element(By.XPATH, "/html/body/div/div").text :
            return (True, data)
        else:
            return (False, 0)
    except:
        return (False, 0)


def login(driver, data):
    try:
        driver.get("http://192.168.0.139:5000/auth/login")
        input_username = driver.find_element(By.XPATH, "/html/body/main/div/form/div[1]/input")
        input_password = driver.find_element(By.XPATH, "/html/body/main/div/form/div[2]/input")
        input_username.send_keys(data['login'])
        input_password.send_keys(data['password'])
        driver.find_element(By.XPATH, "/html/body/main/div/form/button").click()
        if "Вы успешно аутентифицированы." in driver.find_element(By.XPATH, "/html/body/div/div").text:
            return True
        else:
            return False
    except:
        return False
