from calculator.calculator import Calculator
import pytest

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected

    
    def test_subt(self):
        # arrange
        c = 3333
        d = 2222
        cal = Calculator()

        # act
        result = cal.subtract(c, d)

        # assert
        expected2 = 1111
        assert result == expected2


    def test_multip(self):
        # arrange
        e = 9
        f = 8
        cal = Calculator()

        # act
        result = cal.multiply(e, f)

        # assert
        expected3 = 72
        assert result == expected3

    
    def test_deveed(self):
        # arrange
        g = 4
        h = 2
        cal = Calculator()

        # act
        result = cal.divide(g, h)

        # assert
        expected4 = 2
        assert result == expected4

        


    def test_deveed_zero(self):
        # arrange
        i = 2
        j = 0
        cal = Calculator()

        # act and assert
        with pytest.raises(ZeroDivisionError):
            cal.divide(i, j)

        



