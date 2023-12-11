# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Employee Review Application (Processing Class Test File)
# # Description: The unit test file for the processing class python file for the employee registration program
# ChangeLog: (Who, When, What)
# Alexander R. Clark,10Dec2023, Created script
# ------------------------------------------------------------------------------------------------- #

import json
import unittest
import tempfile
from processing_classes import FileProcessor
from data_classes import Employee


class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name

    def tearDown(self):
        pass

    def test_read_employee_data_from_file(self):
        """
        Unit Test to test the read_data_from_file function.  A sample set of data is created to be writen to a temporary
        file.  The file is then read and stored in employees.  The sample set is then compared to the employees list
        to confirm it is the same length and that all values are equal in comparison.

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        sample_data = [{"FirstName": "Alex", "LastName": "Clark", "ReviewDate": "2022-01-09", "ReviewRating": 4},
                       {"FirstName": "Feon", "LastName": "Shu", "ReviewDate": "2022-01-21", "ReviewRating": 5}
                       ]
        employees: list = []  # a table of employee data

        with open(self.temp_file_name, 'w') as file:
            json.dump(sample_data, file)

        employees = FileProcessor.read_employee_data_from_file(file_name=self.temp_file_name, employee_data=employees,
                                                               employee_type=Employee)

        self.assertEqual(len(sample_data), len(employees))

        for i in range(len(sample_data)):
            self.assertEqual(sample_data[i]["FirstName"], employees[i].first_name)
            self.assertEqual(sample_data[i]["LastName"], employees[i].last_name)
            self.assertEqual(sample_data[i]["ReviewDate"], employees[i].review_date)
            self.assertEqual(sample_data[i]["ReviewRating"], employees[i].review_rating)

    def test_read_employee_data_from_file_invalid_json(self):
        """
        Unit Test to test the read_data_from_file function if an invalid JSON file is read.  A temp file is created in
        the wrong format and then read using the read_employee_data_from_file function.  When this function is ran this
        way the program should return a blank list resetting the file to [].  A test is ran to confirm the list len is
        0.

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        with open(self.temp_file_name, 'w') as file:
            file.write("invalid file")

        employees: list = []  # a table of employee data

        employees = FileProcessor.read_employee_data_from_file(file_name=self.temp_file_name, employee_data=employees,
                                                               employee_type=Employee)

        self.assertEqual(0, len(employees))

    def test_read_employee_data_from_file_file_not_found(self):
        """
        Unit Test to test the read_data_from_file function if file is not found.  In this test the file name is modified
        to a name that will not be located and the employees list is checked on whether it's length is zero

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        employees: list = []  # a table of employee data

        employees = FileProcessor.read_employee_data_from_file(file_name="name", employee_data=employees,
                                                               employee_type=Employee)

        self.assertEqual(0, len(employees))

    def test_write_employee_data_to_file(self):
        """
        Unit Test to test the write_employee_data_to_file function.  A sample set of a list of Employees is made
        to write to a temporary file.  The file is then read and loaded into file data.  The original sample data is
        then compared to the data in file_data to compare len and to ensure each value is the same on every
        iteration and keyword.

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        sample_data = [Employee("Alex", "Clark", "2022-01-09", 4),
                       Employee("Jeff", "Shu", "2022-01-09", 5)
                       ]

        FileProcessor.write_employee_data_to_file(file_name=self.temp_file_name, employee_data=sample_data)

        with open(self.temp_file_name, "r") as file:
            file_data = json.load(file)

        self.assertEqual(len(sample_data), len(file_data))

        for i in range(len(sample_data)):
            self.assertEqual(file_data[i]["FirstName"], sample_data[i].first_name)
            self.assertEqual(file_data[i]["LastName"], sample_data[i].last_name)
            self.assertEqual(file_data[i]["ReviewDate"], sample_data[i].review_date)
            self.assertEqual(file_data[i]["ReviewRating"], sample_data[i].review_rating)


if __name__ == "__main__":
    unittest.main()
