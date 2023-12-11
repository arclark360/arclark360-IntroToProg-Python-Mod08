# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08-Employee Review Application (Main File)
# # Description: The main python file for the employee registration program
# ChangeLog: (Who, When, What)
# Alexander R. Clark,10Dec2023, Created script
# ------------------------------------------------------------------------------------------------- #

from data_classes import Employee
from processing_classes import FileProcessor
from presentation_classes import IO

# Constants & Variables
FILE_NAME: str = 'EmployeeRatings.json'

MENU: str = '''
---- Employee Ratings ------------------------------
  Select from the following menu:
    1. Show current employee rating data.
    2. Enter new employee rating data.
    3. Save data to a file.
    4. Exit the program.
--------------------------------------------------
'''

employees: list = []  # a table of employee data
menu_choice = ''

# Start of the program in which it attempts to read the employee JSON File
employees = FileProcessor.read_employee_data_from_file(file_name=FILE_NAME,
                                                       employee_data=employees,
                                                       employee_type=Employee)

# Start of the menu choice loop where actions are chosen based on the users input
while True:

    #Outputs menu at the start of every loop iteration
    IO.output_menu(menu=MENU)

    #Stores the users menu option
    menu_choice = IO.input_menu_choice()

    # Displays current stored employees
    if menu_choice == "1":
        try:
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        continue
    # Captures new employee data and adds it to the list as well as displays updated list
    elif menu_choice == "2":
        try:
            employees = IO.input_employee_data(employee_data=employees,
                                               employee_type=Employee)
            IO.output_employee_data(employee_data=employees)
        except Exception as e:
            IO.output_error_messages(e)
        continue
    # Saves the current stored list of Employees to a JSON file
    elif menu_choice == "3":
        try:
            FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {FILE_NAME} file.")
        except Exception as e:
            IO.output_error_messages(e)
        continue
    # End the program
    elif menu_choice == "4":
        break  # out of the while loop
