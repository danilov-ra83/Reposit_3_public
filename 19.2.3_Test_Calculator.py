import pytest
from app import calculator
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4 # Тест на умножение

    def test_multiply_calculate_faild(self): # Негативный тест на умножение
        assert self.calc.multiply(self, 2, 2) == 5

    def test_division_calculate_correctly(self): # Тест на проверку правильности деления
        assert self.calc.division(self, 6, 2) == 3

    def test_subtraction_calculate_correctly(self): # Тест на проверку правильности вычитания
        assert self.calc.subtraction(self, 7, 2) == 5

    def test_adding_calculate_correctly(self): # Тест на проверку правильности сложения
        assert self.calc.adding(self, 4, 2) == 6
