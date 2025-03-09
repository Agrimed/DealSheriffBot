from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

driver = webdriver.Chrome()

while True:

    advertisement = input().replace(" ", "+")
    driver.get(f"https://www.avito.ru/all?q={advertisement}")

    no_results = driver.find_elements(By.CSS_SELECTOR, ".no-results-title-jho0M")
    if no_results:
        print("Ничего не найдено в выбранной области поиска")
        print("Введите номер корректного объявления")
        continue

    # Поиск объявлений
    elements = driver.find_elements(By.CSS_SELECTOR, ".iva-item-sliderLink-Fvfau")
    first_element = elements[0]
    link = first_element.get_attribute("href")
    print(f"Переход по ссылке: {link}")
    driver.get(link)
