# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Employee Review Application (Data Class File)
# # Description: The data class python file for the employee registration program
# ChangeLog: (Who, When, What)
# Alexander R. Clark,10Dec2023, Created script
# ------------------------------------------------------------------------------------------------- #

from datetime import date


# Person is the parent class of Employee
class Person:
    """
    A class representing person data.

    Properties:
    - first_name (str): The person's first name.
    - last_name (str): The person's last name.

    ChangeLog:
    Alexander R. Clark, 10Dec2023: Created the class.
    """

    # initializer for Person with first and Last name parameters
    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name

    @property
    # getter for first name which capitalizes the first char and lowercase's all other
    def first_name(self):
        return self.__first_name.title()

    @first_name.setter
    # setter for first name which checks to see if it's alphabetic and raises error if it is not
    def first_name(self, value: str):
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")

    @property
    # getter for last name which capitalizes the first char and lowercase's all other
    def last_name(self):
        return self.__last_name.title()

    @last_name.setter
    # setter for last name which checks to see if it's alphabetic and raises error if it is not
    def last_name(self, value: str):
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")

    def __str__(self):
        return f"{self.first_name},{self.last_name}"


# Employee is a subclass of Person and will inherit its attributes
class Employee(Person):
    """
    A subclass representing employee data.

    Properties:
    - first_name (str): The employee's first name.
    - last_name (str): The employee's last name.
    - review_date (date): The data of the employee review.
    - review_rating (int): The review rating of the employee's performance (1-5)

    ChangeLog:
    Alexander R. Clark, 10Dec2023: Created the class.
    """

    # initializer for Employee with first and last name are inherited from Person and date and rating are unique to the
    # subclass
    def __init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01",
                 review_rating: int = 3):

        super().__init__(first_name=first_name, last_name=last_name)
        self.review_date = review_date
        self.review_rating = review_rating

    @property
    # getter for review date
    def review_date(self):
        return self.__review_date

    @review_date.setter
    # setter for review date which ensures date is in the ISO format.  If not it raises a value error.
    def review_date(self, value: str):
        try:
            date.fromisoformat(value)
            self.__review_date = value
        except ValueError:
            raise ValueError("Incorrect data format, should be YYYY-MM-DD")

    @property
    # getter for review rating
    def review_rating(self):
        return self.__review_rating

    @review_rating.setter
    # setter for review rating which checks to see if the value is 1-5
    def review_rating(self, value: str):
        if value in (1, 2, 3, 4, 5):
            self.__review_rating = value
        else:
            raise ValueError("Please choose only values 1 through 5")

    def __str__(self):
        return f"{self.first_name},{self.last_name},{self.review_date},{self.__review_rating}"
