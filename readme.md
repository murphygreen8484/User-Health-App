# User Health app
**written by Dan Murphy**
_September 2024_


---
## Health Class:
(_located in directory health_class_)

<ins>Parameters:</ins>
 - weight: float
 - height: float
 - age: int
 - gender: ENUM

<ins>Methods:</ins>
 - calc_male_SI_BMR
 - calc_male_US_BMR
 - calc_female_SI_BMR
 - calc_female_US_BMR
 - calc_male_SI_BMI
 - calc_male_US_BMI
 - calc_female_SI_BMI
 - calc_female_US_BMI
 - calc_male_SI_LBI
 - calc_male_US_LBI
 - calc_female_SI_LBI
 - calc_female_US_LBI

*NOTE: understood that male/female BMI is the same,
created both instances to allow for better dictionary
searches of functions within Person class.

*NOTE: Many/Most of these calculations are incorrect. This was
mostly an exercise in syntax rather than actual usable calculator.
Please feel free to fork/edit any/all of the calculations.

---
## Person Class:
(_located in directory user_class_)

<ins>Parameters:</ins>
 - name: str
 - age: int
 - height: float
 - weight: float
 - gender: ENUM
 - units_of_measure: ENUM
 - user_health: Callable[Health]
 - func_dict: dict[str, Callable]

<ins>ENUMS</ins>
~~~
class MeasureUnits(StrEnum):
    SI: str = "SI"
    US: str = "US"
~~~

~~~
class Gender(StrEnum):
    MALE: str = "male"
    FEMALE: str = "female"
~~~
