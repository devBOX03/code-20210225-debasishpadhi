# Python code to demonstrate working of unittest 
import unittest
from bmicalculator.bmi_calculator import BMICalculator

class TestGetReportDataMethod(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty_string(self):
        self.assertEqual(([], 'missing data'), BMICalculator('').get_bmi_report())

    def test_none_value(self):
        self.assertEqual(([], 'missing data'), BMICalculator(None).get_bmi_report())

    def test_invalid_data(self):
        self.assertEqual(([], 'invalid data'), BMICalculator('{a: 1}').get_bmi_report())

    def test_single_record(self):
        test_report_data = '[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }]'
        final_report = ([{'Gender': 'Male', 'HeightCm': 171, 'WeightKg': 96, 'BMI': 32.83,
                          'BMICategory': 'Moderately obese', 'HealthRisk': 'Medium risk'}],
                        'final data')
        self.assertEqual(final_report, BMICalculator(test_report_data).get_bmi_report())

    def test_multiple_records(self):
        test_report_data = '''
[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg":85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166,"WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female","HeightCm": 167, "WeightKg": 82}]
'''
        final_report = ([{'Gender': 'Male', 'HeightCm': 171, 'WeightKg': 96, 'BMI': 32.83,
                          'BMICategory': 'Moderately obese', 'HealthRisk': 'Medium risk'},
                         {'Gender': 'Male', 'HeightCm': 161, 'WeightKg': 85, 'BMI': 32.79, 
                          'BMICategory': 'Moderately obese', 'HealthRisk': 'Medium risk'},
                         {'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 77, 'BMI': 23.77,
                          'BMICategory': 'Normal weight', 'HealthRisk': 'Low risk'},
                         {'Gender': 'Female', 'HeightCm': 166, 'WeightKg': 62, 'BMI': 22.5,
                          'BMICategory': 'Normal weight', 'HealthRisk': 'Low risk'},
                         {'Gender': 'Female', 'HeightCm': 150, 'WeightKg': 70, 'BMI': 31.11,
                          'BMICategory': 'Moderately obese', 'HealthRisk': 'Medium risk'},
                         {'Gender': 'Female', 'HeightCm': 167, 'WeightKg': 82, 'BMI': 29.4,
                          'BMICategory': 'Overweight', 'HealthRisk': 'Enhanced risk'}],
                        'final data')
        self.assertEqual(final_report, BMICalculator(test_report_data).get_bmi_report())


if __name__ == '__main__':
    unittest.main() 
