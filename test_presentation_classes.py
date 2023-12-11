# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Employee Review Application (Presentation Class Test File)
# # Description: The unit test file for the presentation class python file for the employee registration program
# ChangeLog: (Who, When, What)
# Alexander R. Clark,10Dec2023, Created script
# ------------------------------------------------------------------------------------------------- #

import unittest
from unittest.mock import patch
from presentation_classes import IO
from data_classes import Employee
from io import StringIO


class TestIOProcessor(unittest.TestCase):

    def test_input_menu_choice(self):
        """
        Unit test to verify the input_menu_choice function is storing the appropriate value.  If 2 is not returned then
        it fails the test

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        with patch("builtins.input", return_value="2"):
            choice = IO.input_menu_choice()
            self.assertEqual("2", choice)

    def test_input_employee_data(self):
        """
        Unit test to verify the input_employee_data function is storing the appropriate value.  It is patched a test
        sample then each value is tested against the expected value

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        with patch("builtins.input", side_effect=["Alex", "Clark", "2023-01-01", 5]):
            employees = []
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)
            self.assertEqual(1, len(employees))
            self.assertEqual("Alex", employees[0].first_name)
            self.assertEqual("Clark", employees[0].last_name)
            self.assertEqual("2023-01-01", employees[0].review_date)
            self.assertEqual(5, employees[0].review_rating)

    def test_input_employee_data_invalid_date(self):
        """
        Unit test to verify the input_employee_data function will not store a value if incorrect data is entered.
        It is patched a test sample that has an error in the data value and will pass the test if the list is length 0

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        with patch("builtins.input", side_effect=["Alex", "Clark", "25343", 5]):
            employees = []
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)
            self.assertEqual(0, len(employees))

    def test_input_employee_data_invalid_rating(self):
        """
        Unit test to verify the input_employee_data function will not store data if invalid rating is used.  The sample
        data is given a rating of 6 to test that when used the employee object is not created and list remains len 0

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        with patch("builtins.input", side_effect=["Alex", "Clark", "2023-01-01", 6]):
            employees = []
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)
            self.assertEqual(0, len(employees))

    def test_output_menu(self):
        """
        Unit test to verify the format of the output menu is correct.  Tests the output_menu on a sample of the test
        MENU constant.  The output from the console is then stored in actual_output and tested against the curated
        string in the expected_output value.

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        with patch("sys.stdout", new_callable=StringIO) as mock:
            prompt = '''
            ---- Employee Ratings ------------------------------
            Select from the following menu:
            1. Show current employee rating data.
            2. Enter new employee rating data.
            3. Save data to a file.
            4. Exit the program.
            --------------------------------------------------
            '''
            IO.output_menu(prompt)
        actual_output = mock.getvalue()
        expected_output = f"\n{prompt}\n\n"
        self.assertEqual(expected_output, actual_output)

    def test_output_employee_data(self):
        """
        Unit test to verify the format of the output_employee_data function is correct. A sample list is created and
        passed to the output_employee_data function.  The output from the function is collected in actual_output and
        then compared to the expected_output string to ensure the format of the output is correct.

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        with patch("sys.stdout", new_callable=StringIO) as mock:

            employees =[Employee("Alex", "Clark", "2024-01-01", 5)]
            IO.output_employee_data(employee_data=employees)

        actual_output = mock.getvalue()
        expected_output = ("\n--------------------------------------------------\n Alex Clark is rated as 5 ("
                           "Leading)\n--------------------------------------------------\n\n")
        self.assertEqual(expected_output, actual_output)


if __name__ == "__main__":
    unittest.main()
