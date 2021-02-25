from setuptools import setup

setup(name="bmicalculator",
      version="0.2",
      description="This package helps to calculate BMI",
      long_description="This package helps to calculate Body Mass Index by considering height and weight",
      author="Debasish Padhi",
      packages=["bmicalculator"],
      install_requires="nose",
      test_suite='nose.collector',
      tests_require=['nose'],)
