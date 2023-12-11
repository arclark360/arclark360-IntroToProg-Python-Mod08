# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Employee Review Application (Presentation Class File)
# # Description: The presentation class python file for the employee registration program
# ChangeLog: (Who, When, What)
# Alexander R. Clark,10Dec2023, Created script
# ------------------------------------------------------------------------------------------------- #

from data_classes import Employee


class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    Alexander R. Clark, 10Dec2023: Created the class.
    """
    pass

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the custom error messages to the user

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the class.

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        # Prints the custom message as well as information regarding the error type

        try:
            print(message, end="\n\n")
            if error is not None:
                print(message)
                print(error, error.__doc__, type(error), sep='\n')
        except Exception as e:
            IO.output_error_messages(e.__str__())

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the class.

        :return: None
        """
        try:
            print()
            print(menu)
            print()
        except Exception as e:
            IO.output_error_messages(e.__str__())

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the class.

        :return: string with the users choice
        """
        # Resets choice to zero then collects new input.  If not 1-4 it will raise an exception.
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # passing the exception object to avoid the technical message

        return choice

    @staticmethod
    def output_employee_data(employee_data: list):
        """ This function displays employee data to the user

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the class.

        :param employee_data: list of employee object data to be displayed

        :return: None
        """
        try:
            message: str = ''
            print()
            print("-" * 50)
            # Iterates over the employee list creating a unique message based on the employee's rating using the .format()
            # method
            for employee in employee_data:
                if employee.review_rating == 5:
                    message = " {} {} is rated as 5 (Leading)"
                elif employee.review_rating == 4:
                    message = " {} {} is rated as 4 (Strong)"
                elif employee.review_rating == 3:
                    message = " {} {} is rated as 3 (Solid)"
                elif employee.review_rating == 2:
                    message = " {} {} is rated as 2 (Building)"
                elif employee.review_rating == 1:
                    message = " {} {} is rated as 1 (Not Meeting Expectations"

                print(message.format(employee.first_name, employee.last_name, employee.review_date,
                                     employee.review_rating))
            print("-" * 50)
            print()
        except Exception as e:
            IO.output_error_messages(e.__str__())


    @staticmethod
    def input_employee_data(employee_data: list, employee_type: Employee):
        """ This function gets the first name, last name, review date, and review rating for the employee

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the class.

        :param employee_data: list of Employee data to be filled with input data

        :return: list
        """

        try:
            # Gets Input from the user for each parameter of the Employee Class and adds the object to the list
            employee_object = employee_type()
            employee_object.first_name = input("What is the employee's first name? ")
            employee_object.last_name = input("What is the employee's last name? ")
            employee_object.review_date = input("What is their review date? ")
            employee_object.review_rating = int(input("What is their review rating? "))
            employee_data.append(employee_object)

        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)

        return employee_data
