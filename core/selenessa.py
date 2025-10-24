from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


class BrowserSession:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()


def login(driver, url, user, password):
    driver.get(url)
    wait = WebDriverWait(driver, 30)
    username_field = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@placeholder='Пользователь']")
        )
    )
    password_field = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Пароль']"))
    )
    submit_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//input[@value='Войти']"))
    )
    username_field.send_keys(user)
    password_field.send_keys(password)
    submit_button.click()


# def logout(driver):
#     wait = WebDriverWait(driver, 20)
#     logout_button = wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//div[@id='LogoutButton']"))
#     )
#     logout_close_button = wait.until(
#         EC.element_to_be_clickable((By.XPATH, "//div[@id='LogoutCloseButton']"))
#     )
#     logout_button.click()
#     logout_close_button.click()
#     # Принять alert (нажать OK)

#     alert = driver.switch_to.alert
#     alert.accept()


def left_menu_click(driver, item):
    wait = WebDriverWait(driver, 40)
    xpath = f"//div[@class='themeBoxName' and contains(., '{item}')]"
    left_menu_el = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    left_menu_el.click()


def search(driver, item):
    wait = WebDriverWait(driver, 30)
    search_field = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//input[@id='funcPanel_panelEdit_i0']")
        )
    )
    item = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='cmd_0_0_0_txt']"))
    )
    search_field.send_keys(item)


if __name__ == "__main__":
    with BrowserSession() as driver:
        login(
            driver,
            "https://1cfresh.com/a/ea/3654418",
            "nick.bog.17@yandex.ru",
            "2aoqEls",
        )
        left_menu_click(driver, "Главное")
        search(driver, "Платежные поручения")
        input("Нажмите Enter, чтобы закрыть браузер...")
