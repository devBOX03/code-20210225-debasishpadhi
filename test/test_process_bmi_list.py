# Python code to demonstrate working of unittest 
import unittest
from bmicalculator.bmi_calculator import BMICalculator

class TestGetReportDataMethod(unittest.TestCase):
    def setUp(self):
        pass

    def test_invalid_empty_list(self):
        self.assertEqual(([], 0), BMICalculator.process_bmi_list(''))
        self.assertEqual(([], 0), BMICalculator.process_bmi_list('abc'))
        self.assertEqual(([], 0), BMICalculator.process_bmi_list(None))
        self.assertEqual((['abcd'], 0), BMICalculator.process_bmi_list(['abcd']))

    def test_single_record(self):
        test_report_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 }]
        test_report_data_2 = [{"Gender": "Male", "HeightCm": None, "WeightKg": 96 }]
        final_report = ([{'Gender': 'Male', 'HeightCm': 171, 'WeightKg': 96, 'BMI': 32.83,
                          'BMICategory': 'Moderately obese', 'HealthRisk': 'Medium risk'}],
                        0)
        final_report_2 = ([{'Gender': 'Male', 'HeightCm': None, 'WeightKg': 96, 'BMI': None,
                          'BMICategory': None, 'HealthRisk': None}],
                        0)
        self.assertEqual(final_report, BMICalculator.process_bmi_list(test_report_data))
        self.assertEqual(final_report_2, BMICalculator.process_bmi_list(test_report_data_2))

    def test_multiple_records(self):
        test_report_data = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
                            { "Gender": "Male", "HeightCm": 161, "WeightKg":85 },
                            { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
                            { "Gender": "Female", "HeightCm": 166,"WeightKg": 62},
                            {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
                            {"Gender": "Female","HeightCm": 167, "WeightKg": 82}]
        test_report_data_2 = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
                            { "Gender": "Male", "HeightCm": 161, "WeightKg":None },
                            { "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
                            { "Gender": "Female", "HeightCm": 166,"WeightKg": 62},
                            {"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
                            {"Gender": "Female","HeightCm": 167, "WeightKg": '82kg'}]

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
                        1)
        final_report_2 = ([{'Gender': 'Male', 'HeightCm': 171, 'WeightKg': 96, 'BMI': 32.83,
                          'BMICategory': 'Moderately obese', 'HealthRisk': 'Medium risk'},
                         {'Gender': 'Male', 'HeightCm': 161, 'WeightKg': None, 'BMI': None, 
                          'BMICategory': None, 'HealthRisk': None},
                         {'Gender': 'Male', 'HeightCm': 180, 'WeightKg': 77, 'BMI': 23.77,
                          'BMICategory': 'Normal weight', 'HealthRisk': 'Low risk'},
                         {'Gender': 'Female', 'HeightCm': 166, 'WeightKg': 62, 'BMI': 22.5,
                          'BMICategory': 'Normal weight', 'HealthRisk': 'Low risk'},
                         {'Gender': 'Female', 'HeightCm': 150, 'WeightKg': 70, 'BMI': 31.11,
                          'BMICategory': 'Moderately obese', 'HealthRisk': 'Medium risk'},
                         {'Gender': 'Female', 'HeightCm': 167, 'WeightKg': '82kg', 'BMI': None,
                          'BMICategory': None, 'HealthRisk': None}],
                        0)

        self.assertEqual(final_report, BMICalculator.process_bmi_list(test_report_data))
        self.assertEqual(final_report_2, BMICalculator.process_bmi_list(test_report_data_2))


if __name__ == '__main__':
    unittest.main() 
