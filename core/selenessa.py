from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_selenium_simple():
    # Убедитесь, что chromedriver установлен в PATH
    driver = webdriver.Chrome()  # или webdriver.Firefox()
    
    try:
        driver.get("https://www.python.org")
        print(f"Сайт загружен: {driver.title}")
        
        # Ищем логотип Python
        logo = driver.find_element(By.CLASS_NAME, "python-logo")
        print("Логотип Python найден!")
        
        # Делаем скриншот
        driver.save_screenshot("python_org.png")
        print("Скриншот сохранен!")
        
    except Exception as e:
        print(f"Ошибка: {e}")
        
    finally:
        driver.quit()

if __name__ == "__main__":
    test_selenium_simple()