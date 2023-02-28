import  pytest

from app.calc import Calculator

class Test:
    def setup(self):
        self.calc = Calculator

    def test_sum(self):
        assert self.calc.adding(self, 2, 2) == 4

    def test_subtraction(self):
        assert self.calc.subtraction(self, 21, 3) == 18

    def test_division(self):
        assert self.calc.division(self, 21, 3) == 7

    def test_multiplication(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def teardown(self):
        print('Выполнение метода Teardown')

