import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_there_is_a_name_age_and_gender(go_to_my_pets):
   '''Поверяем, что на странице со списком моих питомцев, у всех питомцев есть имя, возраст и порода'''

   element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   # Сохраняем в переменную pet_data элементы с данными о питомцах
   # pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   element = WebDriverWait(pytest.driver, 15).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
   # Нажимаем на ссылку "Мои питомцы"
   pytest.driver.find_element(By.LINK_TEXT, "Мои питомцы").click()
   pet_data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   # Перебираем данные из pet_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
   # и разделяем по пробелу. Находим кол-во элементов в получившемся списке и сравниваем их
   # с ожидаемым результатом
   for i in range(len(pet_data)):
      data_pet = pet_data[i].text.replace('\n', '').replace('×', '')
      split_data_pet = data_pet.split(' ')
      result = len(split_data_pet)
      assert result == 4

# python -m pytest -v --driver Chrome --driver-path /SkillFactory/test_driver/chromedriver.exe tests/test_with_name_age_gender.py