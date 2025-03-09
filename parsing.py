from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

driver = webdriver.Chrome()
try:
    advertisement = input().replace(" ", "+")
    driver.get(f"https://www.avito.ru/all?q={advertisement}")

    # Используем явное ожидание для поиска элементов
    elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".iva-item-sliderLink-Fvfau")
        )
    )
        
        # Проверяем, что элементы найдены
    if elements:
        first_element = elements[0]  # Берем первый элемент
        link = first_element.get_attribute("href")
        print(f"Переход по ссылке: {link}")
        driver.get(link)
    else:
        print("Объявления не найдены")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Вопрос о закрытии браузера: если нужно остаться на странице — уберите driver.quit()
    # driver.quit()
    pass

input("Enter")
driver.quit()