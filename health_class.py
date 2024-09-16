from dataclasses import dataclass


@dataclass(kw_only=True)
class Health:
    """
    Parameters
    ----------
    weight
    height
    age
    gender
    """
    weight: float
    height: float
    age: int
    gender: str

    def calc_male_SI_BMR(self) -> float:
        """Takes the weight kg and height cm and calculates the BRM for a male.

        Returns
        -------
        (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5
         """

        return (10 * self.weight) + (6.25 * self.height) - (5 * self.age) + 5

    def calc_male_US_BMR(self) -> float:
        """Takes the weight lbs and height inches and calculates the BRM for a male.

        Returns
        -------
        round((6.24 * self.weight) + (12.7 * self.height) - (6.76 * self.age) + 66.47, 2)
         """

        return round((6.24 * self.weight) + (12.7 * self.height) - (6.76 * self.age) + 66.47, 2)

    def calc_female_US_BMR(self) -> float:
        """Takes the weight lbs and height inches and calculates the BRM for a female.

        Returns
        -------
        round((4.34 * self.weight) + (4.7 * self.height) - (4.7 * self.age) + 65.51, 2)
         """

        return round((4.34 * self.weight) + (4.7 * self.height) - (4.7 * self.age) + 65.51, 2)

    def calc_female_SI_BMR(self) -> float:
        """Takes the weight kg and height cm and calculates the BRM for a female.

        Returns
        -------
        (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161
         """

        return (10 * self.weight) + (6.25 * self.height) - (5 * self.age) - 161

    def calc_male_SI_BMI(self) -> float:
        """Takes the weight kg and height m and calculates the BMI.

        Returns
        -------
        (round(self.weight / height_meters, 2))**2
        """

        height_meters = round(self.height * 0.01, 2)

        try:
            return round((round(self.weight / height_meters, 2)) ** 2, 2)
        except ZeroDivisionError as z:
            return z

    def calc_female_SI_BMI(self) -> float:
        """Takes the weight kg and height m and calculates the BMI.

        Returns
        -------
        (round(self.weight / height_meters, 2))**2
        """

        height_meters = round(self.height * 0.01, 2)

        try:
            return round((round(self.weight / height_meters, 2)) ** 2, 2)
        except ZeroDivisionError as z:
            return z

    def calc_male_US_BMI(self) -> float:
        """Takes the weight lbs and height inches and calculates the BMI.

        Returns
        -------
        (round(self.weight / (self.height ** 2), 2)) * 703
        """

        try:
            return (round(self.weight / (self.height ** 2), 2)) * 703
        except ZeroDivisionError as z:
            return z

    def calc_female_US_BMI(self) -> float:
        """Takes the weight lbs and height inches and calculates the BMI.

        Returns
        -------
        (round(self.weight / (self.height ** 2), 2)) * 703
        """

        try:
            return (round(self.weight / (self.height ** 2), 2)) * 703
        except ZeroDivisionError as z:
            return z

    def calc_male_SI_LBI(self) -> float:
        """Takes the weight kg and height cm and calculates the Lean Body Mass for males.

        Returns
        -------
        round((0.32810 * self.weight) + (0.33929 * self.height) - 29.5336, 2)
        """
        return round((0.32810 * self.weight) + (0.33929 * self.height) - 29.5336, 2)

    def calc_female_SI_LBI(self) -> float:
        """Takes the weight kg and height cm and calcculates the Lean Body Mass for females.

        Returns
        -------
        round((0.29569 * self.weight) + (0.41813 * self.height) - 43.2933, 2)
        """
        return round((0.29569 * self.weight) + (0.41813 * self.height) - 43.2933, 2)

    def calc_male_US_LBI(self) -> float:
        """Takes the weight lbs and height inches and calculates the Lean Body Mass for males.

        Returns
        -------
        round((0.32810 * self.weight) + (0.33929 * self.height) - 29.5336, 2)
        """
        return round((0.32810 * self.weight) + (0.33929 * self.height) - 29.5336, 2)

    def calc_female_US_LBI(self) -> float:
        """Takes the weight lbs and height inches and calcculates the Lean Body Mass for females.

        Returns
        -------
        round((0.29569 * self.weight) + (0.41813 * self.height) - 43.2933, 2)
        """
        return round((0.29569 * self.weight) + (0.41813 * self.height) - 43.2933, 2)


if __name__ == '__main__':
    ...
