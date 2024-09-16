from typing import Callable

from health_class import Health
from enum import StrEnum


class MeasureUnits(StrEnum):
    SI: str = "SI"
    US: str = "US"


class Gender(StrEnum):
    MALE: str = "male"
    FEMALE: str = "female"


class Person:
    def __init__(self, name: str, age: int, height: float, weight: float, gender: Gender,
                 units_of_measure: MeasureUnits, health: Health):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender
        self.units_of_measure = units_of_measure
        self.user_health = health
        self.func_dict: dict[str, Callable] = self.make_func_table()

    def make_func_table(self) -> dict[str, Callable]:
        func_dict: dict[str, Callable] = dict()
        func: str
        for func in dir(self.user_health):
            if func[:5] == "calc_":
                func_dict[func] = getattr(self.user_health, func)

        return func_dict

    @classmethod
    def get_name(cls):
        while True:
            name = input("Enter your name: ")
            if name.replace(" ", "").isalpha():
                return name
            else:
                print("Please enter a name with letters only")

    @classmethod
    def get_age(cls):
        while True:
            try:
                age = int(input("Enter your age in years: "))
                if 0 < age < 120:
                    return age
                else:
                    print("Please enter a valid age in whole years")
            except ValueError:
                print("Please enter numbers only.")

    @classmethod
    def get_weight(cls, units: MeasureUnits):

        weight_unit = "kg" if units == MeasureUnits.SI else "lb"

        while True:
            try:
                weight = float(input(f"Enter your weight in {weight_unit}: "))
                if weight > 0:
                    return weight
                else:
                    print(f"Please enter a valid weight in {weight_unit}")
            except ValueError:
                print("Please enter numbers only.")

    @classmethod
    def get_height(cls, units: MeasureUnits):

        height_unit = "cm" if units == MeasureUnits.SI else "inches"

        while True:
            try:
                height = float(input(f"Enter your height in {height_unit}: "))
                if height > 0:
                    return height
                else:
                    print(f"Please enter a valid height in {height_unit}")
            except ValueError:
                print("Please enter numbers only.")

    @classmethod
    def get_gender(cls) -> Gender:
        while True:
            user_gender: str = input("Enter your gender [male, female]: ")
            if user_gender.lower()[0] == "m":
                return Gender.MALE
            if user_gender.lower()[0] == "f":
                return Gender.FEMALE
            else:
                print("Currently this program only works with male or female. Please pick one.")

    @classmethod
    def get_units(cls) -> MeasureUnits:
        while True:
            unit_of_measure = input("Enter your preferred unit of measure [SI, US]: ")
            if unit_of_measure == "SI":
                return MeasureUnits.SI
            elif unit_of_measure == "US":
                return MeasureUnits.US
            else:
                print("Please enter a valid unit. Either 'SI' or 'US'")

    @classmethod
    def create_person(cls):
        name = cls.get_name()
        age = cls.get_age()
        gender = cls.get_gender()
        units_of_measure = cls.get_units()
        height = cls.get_height(units_of_measure)
        weight = cls.get_weight(units_of_measure)
        health = Health(weight=weight, height=height, age=age, gender=gender)

        return cls(name=name, age=age, gender=gender, height=height, weight=weight,
                   units_of_measure=units_of_measure, health=health)

    def __str__(self) -> str:

        user_bmi = self.func_dict.get(f"calc_{self.gender}_{self.units_of_measure}_BMI")()
        user_bmr = self.func_dict.get(f"calc_{self.gender}_{self.units_of_measure}_BMR")()

        return f"""
            Hello {self.name},
            ---------------------------------
            based on your info:
            Your BMI is: {user_bmi}
            Your BMR is: {user_bmr}
        """


if __name__ == '__main__':
    test_person = Person.create_person()
    print(test_person)
