import pytest
from app.calculator import Calculator   # импортруем функции, которые будем проверять

class TestCalc:     # класс теста всегда начинается с слова Тест + название
    def setup(self):    # подготовительный метод
        self.calc = Calculator  # создаем объект приложения из импортированного класса

    def  test_multiply_calculate_correctly(self):   # функция проверки умножения позитивный сценарий
         assert self.calc.multiply(self, 2, 2) == 4  # assert = сравнивает ожидание с результатом, вызываем провер. метод и передаем туда значения

    def test_multiply_calculation_failed(self):  # функция проверки неготивного сценария
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_calculationcorrectly(self):
        assert self.calc.division(self, 3, 3) == 1

    def test_division_calculation_failed(self):
        assert self.calc.division(self, 3, 2) == 1

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 10, 5) == 5

    def test_subtraction_calculation_failed(self):
        assert self.calc.subtraction(self, 10, 11) == 2

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 5, 5) == 10

    def test_adding_calculation_failed(self):
        assert self.calc.adding(self, 5, 10) == 10