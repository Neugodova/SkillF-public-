import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def test_all_pets_are_present(go_to_my_pets):
   '''Проверяем, что на странице со списком моих питомцев присутствуют все питомцы'''

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   # Сохраняем в переменную stastistic элементы
   statistic = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   # Сохраняем в переменную pets элементы карточек питомцев
   pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Получаем кол-во питомцев из данных статистики
   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

   # Получаем кол-во карточек питомцев
   number_of_pets = len(pets)

   # Проверяем, что кол-во питомцев из статистики совпадает с кол-во карточек питомцев
   assert number == number_of_pets

# python -m pytest -v --driver Chrome --driver-path /SkillFactory/test_driver/chromedriver.exe tests/test_all_pets.py