# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Employee Review Application (Processing Class File)
# # Description: The processing class python file for the employee registration program
# ChangeLog: (Who, When, What)
# Alexander R. Clark,10Dec2023, Created script
# ------------------------------------------------------------------------------------------------- #

from data_classes import Employee
from presentation_classes import IO
import json


class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    Alexander R. Clark, 10Dec2023: Created the class.
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: Employee):
        """ This function reads data from a json file and loads it into a list of dictionaries that is then converted
        into a list of Employees and is returned

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the class.

        :param file_name: string data with name of file to read from
        :param employee_data: list of Employees to be filled with file data
        :param employee_type: a reference to the Employee class
        :return: list
        """
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)  # the load function returns a list of dictionary rows.
                for employee in list_of_dictionary_data:
                    employee_object = employee_type()
                    employee_object.first_name = employee["FirstName"]
                    employee_object.last_name = employee["LastName"]
                    employee_object.review_date = employee["ReviewDate"]
                    employee_object.review_rating = employee["ReviewRating"]
                    employee_data.append(employee_object)
        except FileNotFoundError as e:
            IO.output_error_messages(message="JSON File not found, creating JSON file", error=e)
            json_data = []
            file = open(file_name, "w")
            json.dump(json_data, file)
        except json.decoder.JSONDecodeError as e:
            IO.output_error_messages(message="JSON File invalid, resetting JSON file", error=e)
            json_data = []
            file = open(file_name, "w")
            json.dump(json_data, file)
        except Exception as e:
            IO.output_error_messages(message="There was a non-specific error!", error=e)
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """ This function takes the employee data list and converts it to a list of dictionaries that is then
        saved to the JSON file.

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the class.

        :param file_name: string data with name of file to write to
        :param employee_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            list_of_dictionary_data: list = []
            for employee in employee_data:  # Convert List of employee objects to list of dictionary rows.
                employee_json: dict = {"FirstName": employee.first_name,
                                       "LastName": employee.last_name,
                                       "ReviewDate": employee.review_date,
                                       "ReviewRating": employee.review_rating
                                       }
                list_of_dictionary_data.append(employee_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file)
        except TypeError:
            raise TypeError("Please check that the data is a valid JSON format")
        except PermissionError:
            raise PermissionError("Please check the data file's read/write permission")
        except Exception as e:
            raise Exception("There was a non-specific error!")
