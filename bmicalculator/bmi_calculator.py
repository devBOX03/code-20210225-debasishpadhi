#!/usr/bin/python
'''
@author: Debasish Padhi
@date: 25/02/2021
'''

# Final output Message
MISSING_DATA = "missing data"
INVALID_DATA = "invalid data"
FINAL_DATA = "final data"

# BMI Category
UNDER_WEIGHT = "Underweight"
NORMAL_WEIGHT = "Normal weight"
OVER_WEIGHT = "Overweight"
MODERATELY_OBESE = "Moderately obese"
SEVERELY_OBESE = "Severely obese"
VERY_SEVERELY_OBESE = "Veryseverely obese"

# Health risks
MALNUTRITION_RISK = "Malnutrition risk"
LOW_RISK = "Low risk"
ENHANCED_RISK = "Enhanced risk"
MEDIUM_RISK = "Medium risk"
HIGH_RISK = "High risk"
VERY_HIGH_RISK = "Very high risk"

# BMI values
LOWEST_NORMAL_WEIGHT_BMI = 18.5
LOWEST_OVER_WEIGHT_BMI = 25.0
LOWEST_MODERATELY_OBESE_BMI = 30.0
LOWEST_SEVERELY_OBESE_BMI = 35.0
LOWEST_VERY_SEVERELY_OBESE_BMI = 40.0

# BMI report columns
GENDER = "Gender"
HEIGHT_CM = "HeightCm"
WEIGHT_KG = "WeightKg"
BMI = "BMI"
BMI_CATEGORY = "BMICategory"
HEALTH_RISK = "HealthRisk"

class BMICalculator:
    """
    This class can be used to calculate Body Mass Index(BMI)
    and to prepare reports using it
    """

    def __init__(self, test_report_data):
        self.test_report_data = test_report_data
        self.overweight_people_count = 0

    def get_bmi_report(self):
        """
        get final BMI report out of test report data
        @return (final_report, message)
        @type (list, str)
        """
        final_report = list()

        if not self.test_report_data:
            return (final_report, MISSING_DATA)

        try:
            final_report, self.overweight_people_count = BMICalculator.process_bmi_list(eval(self.test_report_data))
        except Exception:
            return (final_report, INVALID_DATA)
        
        return (final_report, FINAL_DATA)

    @classmethod
    def process_bmi_list(cls, test_report_list):
        """
        prepare BMI list by adding BMI, BMI category and health risk using BMI value

        @param test_report_list
        @type list

        @return list, int
        """
        overweight_people_count = 0

        if not test_report_list or type(test_report_list) is not list:
            return (list(), overweight_people_count)

        for data in test_report_list:
            # ignore if data is not dict
            if type(data) is not dict:
                continue

            bmi = BMICalculator.calculate_bmi(data.get(HEIGHT_CM), data.get(WEIGHT_KG))

            if bmi:
                if bmi < LOWEST_NORMAL_WEIGHT_BMI:
                    bmi_category, health_risk = UNDER_WEIGHT, MALNUTRITION_RISK
                elif bmi >= LOWEST_NORMAL_WEIGHT_BMI and bmi < LOWEST_OVER_WEIGHT_BMI:
                    bmi_category, health_risk = NORMAL_WEIGHT, LOW_RISK
                elif bmi >= LOWEST_OVER_WEIGHT_BMI and bmi < LOWEST_MODERATELY_OBESE_BMI:
                    bmi_category, health_risk = OVER_WEIGHT, ENHANCED_RISK
                    overweight_people_count += 1
                elif bmi >= LOWEST_MODERATELY_OBESE_BMI and bmi < LOWEST_SEVERELY_OBESE_BMI:
                    bmi_category, health_risk = MODERATELY_OBESE, MEDIUM_RISK
                elif bmi >= LOWEST_SEVERELY_OBESE_BMI and bmi < LOWEST_VERY_SEVERELY_OBESE_BMI:
                    bmi_category, health_risk = SEVERELY_OBESE, HIGH_RISK
                elif bmi >= LOWEST_VERY_SEVERELY_OBESE_BMI:
                    bmi_category, health_risk = VERY_SEVERELY_OBESE, VERY_HIGH_RISK
            else:
                bmi_category, health_risk = None, None
            
            data[BMI] = bmi
            data[BMI_CATEGORY] = bmi_category
            data[HEALTH_RISK] = health_risk
        
        return (test_report_list, overweight_people_count)

    @classmethod
    def calculate_bmi(cls, height_cm, weight_kg):
        """
        calculate BMI using hetght and weight

        @param height_cm
        @type float/int

        @return bmi
        @type @float
        """
        if height_cm is None or weight_kg is None:
            return None
        # handle string data
        if type(height_cm) is str or type(weight_kg) is str:
            try:
                height_cm, weight_kg = float(height_cm), float(weight_kg)
            except ValueError:
                return None
            except TypeError:
                return None
        # convert height to meter from centimeter
        height_m = height_cm / 100.0
        # clculate and return bmi value
        return round(weight_kg / (height_m ** 2), 2)    
