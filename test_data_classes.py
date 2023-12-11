# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Employee Review Application (Data Class Test File)
# # Description: The unit test file for the data class python file for the employee registration program
# ChangeLog: (Who, When, What)
# Alexander R. Clark,10Dec2023, Created script
# ------------------------------------------------------------------------------------------------- #

import unittest
from data_classes import Person, Employee


class TestPerson(unittest.TestCase):

    def test_person_init(self):
        """
        Unit test to test the initializer of the Person Class

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        person = Person("Alex", "clark")
        self.assertEqual("Alex", person.first_name)
        self.assertEqual("Clark", person.last_name)

    def test_person_invalid_first_name(self):
        """
        Unit test to test the setter of the first_name property

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        with self.assertRaises(ValueError):
            person = Person("123", "clark")

    def test_person_invalid_last_name(self):
        """
        Unit test to test the setter of the last_name property

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        with self.assertRaises(ValueError):
            person = Person("Alex", "123")

    def test_person_str(self):
        """
        Unit test to test the str attribute of the Person Class

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        person = Person("alex", "clark")
        self.assertEqual("Alex,Clark", str(person))


class TestEmployee(unittest.TestCase):

    def test_employee_init(self):
        """
        Unit test to test the initializer of the Employee Class

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        employee = Employee("alex", "clark", "2023-01-01", 3)
        self.assertEqual("Alex", employee.first_name)
        self.assertEqual("Clark", employee.last_name)
        self.assertEqual("2023-01-01", employee.review_date)
        self.assertEqual(3, employee.review_rating)

    def test_review_date_invalid_type(self):
        """
        Unit test to test the setter of the review_data property

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        with self.assertRaises(ValueError):
            employee = Employee("alex", "clark", "05Jan2023", 3)

    def test_review_rating_invalid_type(self):
        """
        Unit test to test the setter of the review_rating property

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        with self.assertRaises(ValueError):
            employee = Employee("alex", "clark", "05Jan2023", 3.3)

    def test_employee_str(self):
        """
        Unit test to test the str attribute of the Employee Class

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        employee = Employee("alex", "clark", "2023-01-01", 3)
        self.assertEqual("Alex,Clark,2023-01-01,3", str(employee))


if __name__ == "__main__":
    unittest.main()
