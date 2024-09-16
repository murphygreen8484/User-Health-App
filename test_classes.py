import pytest

from health_class import Health
from user_class import Person, MeasureUnits, Gender


@pytest.fixture
def sample_male_si():
    sample_male_si_user = Person(
        name="TEST MALE SI",
        age=35,
        height=165,
        weight=90,
        gender=Gender.MALE,
        units_of_measure=MeasureUnits.SI,
        health=Health(weight=90, height=165, age=35, gender=Gender.MALE)
    )

    return sample_male_si_user


@pytest.fixture
def sample_female_si():
    sample_female_si_user = Person(
        name="TEST FEMALE SI",
        age=28,
        height=135,
        weight=60,
        gender=Gender.FEMALE,
        units_of_measure=MeasureUnits.SI,
        health=Health(weight=60, height=135, age=28, gender=Gender.FEMALE)
    )

    return sample_female_si_user


@pytest.fixture
def sample_male_us():
    sample_male_us_user = Person(
        name="TEST MALE US",
        age=40,
        height=73,
        weight=260,
        gender=Gender.MALE,
        units_of_measure=MeasureUnits.US,
        health=Health(weight=260, height=73, age=40, gender=Gender.MALE)
    )

    return sample_male_us_user


@pytest.fixture
def sample_female_us():
    sample_female_us_user = Person(
        name="TEST FEMALE US",
        age=38,
        height=57,
        weight=150,
        gender=Gender.FEMALE,
        units_of_measure=MeasureUnits.US,
        health=Health(weight=150, height=57, age=38, gender=Gender.FEMALE)
    )

    return sample_female_us_user


def test_male_us_bmi(sample_male_us):
    assert sample_male_us.user_health.calc_male_US_BMI() == 35.15


def test_male_us_bmr(sample_male_us):
    assert sample_male_us.user_health.calc_male_US_BMR() == 2345.57


def test_male_si_bmi(sample_male_si):
    assert sample_male_si.user_health.calc_male_SI_BMI() == 2975.7


def test_male_si_bmr(sample_male_si):
    assert sample_male_si.user_health.calc_male_SI_BMR() == 1761.25
