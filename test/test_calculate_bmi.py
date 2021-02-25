# Python code to demonstrate working of unittest 
import unittest
from bmicalculator.bmi_calculator import BMICalculator

class TestCalculateBMI(unittest.TestCase):
    def setUp(self):
        pass

    def test_none_data(self):
        self.assertEqual(None, BMICalculator.calculate_bmi(None, 96))
        self.assertEqual(None, BMICalculator.calculate_bmi(171, None))

    def test_string_data(self):
        self.assertEqual(32.83, BMICalculator.calculate_bmi('171', 96))
        self.assertEqual(32.83, BMICalculator.calculate_bmi('171', '96'))
        self.assertEqual(None, BMICalculator.calculate_bmi('abc', 96))

    def test_bmi_calculation(self):
        self.assertEqual(32.83, BMICalculator.calculate_bmi(171, 96))
        self.assertEqual(22.5, BMICalculator.calculate_bmi(166, 62))
        self.assertEqual(29.4, BMICalculator.calculate_bmi(167, 82))


if __name__ == '__main__':
    unittest.main() 
