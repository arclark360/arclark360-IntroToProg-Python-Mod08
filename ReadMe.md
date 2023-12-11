# Employee Review Application
## Intro
This is the markup documentation of the Employee Review application for Assignemnt 08.  This document will cover all the
files, classes, and functions that are involved in the makeup of this application.  Will provide all required user inputs
for the functions being used as well as their output.  Code examples will be provided for all classes and functions.

## Files Needed for Application
- main.py
- data_classes.py
- processing_classes.py
- presentation_classes.py

Unit test files used were
- test_data_classes.py
- test_processing_classes.py
- test_presentation_classes.py

# File -> (main.py)
This is the main Python script for the Employee Review Application. It includes functionality for managing employee 
ratings, such as displaying current data, entering new data, saving data to a file, and exiting the program.
## File/Module Dependencies
*Will need to import  classes directly to run the file
- `data_classes.py`: Module containing the `Employee` class
- `processing_classes.py`: Module containing the `FileProcessor` class
- `presentation_classes.py`: Module containing the `IO` class
## Constants and Variables
Constants and Global Variables used in the employee review application:
- `FILE_NAME`: String representing the name of the file to store employee data (`'EmployeeRatings.json'`).
- `MENU`: String representing the menu options for the user.
- `employees`: List containing employee data.
- `menu_choice`: String storing the user's menu choice.
## Execution Layout
1. Import necessary classes and modules:
    ```python
    from data_classes import Employee
    from processing_classes import FileProcessor
    from presentation_classes import IO
    ```
2. Read employee data from a JSON file and initialize the program using the FileProcessor Class:
    ```python
    employees = FileProcessor.read_employee_data_from_file(file_name=FILE_NAME,
                                                           employee_data=employees,
                                                           employee_type=Employee)
    ```
3. Start the menu choice while loop, which will decide which methods need to be run based on user input (menu_choice):
    ```python
    while True:
        # Display menu options
        IO.output_menu(menu=MENU)
    
        # Get user's menu choice
        menu_choice = IO.input_menu_choice()
    
        # Perform actions based on user's choice
        if menu_choice == "1":
            # Display current employee data
            IO.output_employee_data(employee_data=employees)
        elif menu_choice == "2":
            # Enter new employee data
            employees = IO.input_employee_data(employee_data=employees,
                                               employee_type=Employee)
            IO.output_employee_data(employee_data=employees)
        elif menu_choice == "3":
            # Save data to a file
            FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {FILE_NAME} file.")
        elif menu_choice == "4":
            # Exit the program
            break
    ```


# File -> (data_classes.py)
This is the data class Python file for the Employee Review Application. It defines two classes, `Person` and `Employee`, 
representing person and employee data that the employee review application uses to store information on these data objects.
`Employee` is a subclass of `Person` and will inherit its attribute handling for first name and last name from `Person`.
## File/Module Dependencies
Will need to import the date class from datetime.py Module to handle date attribute for the Employee class
- `datetime.py`: Module containing the `date` class
## Person Class
### Code Example
```python
class Person:
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


```
### Description
Parent class of the Employee class and holds information in regard to first and last name.
### Properties
- `first_name` (str): The person's first name.
- `last_name` (str): The person's last name.
### Methods
#### `__init__(self, first_name: str = "", last_name: str = "")`
- Initializer for the `Person` class with first and last name parameters.
#### `__str__(self) -> str`
- Returns a string representation of the person's full name.
### Getters and Setters
#### `first_name` (property)
- Getter: Returns the Employee first name with the first letter capitalize and all other letters lowercase
- Setter: Ensures the name is alphabetic; raises a `ValueError` if not.
#### `last_name` (property)
- Getter: Returns the Employee last name with the first letter capitalize and all other letters lowercase
- Setter: Ensures the name is alphabetic; raises a `ValueError` if not.

## Employee Class
### Code Example
```python
   class Employee(Person):
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

```
### Description
Subclass of the Person Class and houses information on first name, last name, review date, and review rating
### Properties
- `first_name` (str): The employee's first name (inherited from `Person`).
- `last_name` (str): The employee's last name (inherited from `Person`).
- `review_date` (date): The date of the employee review.
- `review_rating` (int): The review rating of the employee's performance (1-5).
### Methods
#### `__init__(self, first_name: str = "", last_name: str = "", review_date: str = "1900-01-01", review_rating: int = 3)`
- Initializer for the `Employee` class with first and last name inherited from `Person` using the super(). command so that
a person is created also whenever an employee is created.  Additional parameters  `Employee` will include the
review date and rating.
#### `__str__(self) -> str`
- Returns a string representation of the employee's data.
### Getters and Setters
#### `review_date` (property)
- Getter: Returns the review date.
- Setter: Ensures the review date is in ISO format; raises a `ValueError` if not.
#### `review_rating` (property)
- Getter: Returns the review rating.
- Setter: Ensures the review rating is within the range 1-5; raises a `ValueError` if not.

## How to use the data_classes.py
1. Import the modules needed for `Person` and `Employee` classes which are:
    ```python
    from datetime import date
    ```
2. Create instances of the classes and use their properties and methods as needed.
    ```python
    # Example usage
    person = Person(first_name="John", last_name="Doe")
    employee = Employee(first_name="Jane", last_name="Doe", review_date="2023-12-10", review_rating=4)
    ```

# File -> (processing_classes.py)
This is the processing class Python file for the Employee Review Application. It includes the `FileProcessor` class, 
which provides functions for reading and writing employee data to a JSON file.
## File/Module Dependencies
*Will need to import  classes for `Employee` and `FileProcessor` directly to run the file while `json.py` can be 
imported entirely
- `data_classes.py`: Module containing the `Employee` class
- `processing_classes.py`: Module containing the `FileProcessor` class
- `json.py`: Module containing the methods for reading and writing JSON Files

## FileProcessor Class
### Description
Contains two methods one for reading JSON files `read_employee_data_from file` and one for writing to JSON files 
`write_employee_data_from_file`.

### Methods
#### 1. Read Employee File Method
#### `read_employee_data_from_file(file_name: str, employee_data: list, employee_type: Employee) -> list`
#### Code Example
```python
    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: Employee):
        
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

```
#### Description
- This function reads data from a JSON file and loads it into a list of dictionaries. The dictionaries are then 
converted into a list of `Employee` objects which is returned at the end of the function.  As seen in the code above
you will use a `for loop` to iterate of the JSON data and create the individual Employee Object for each iteration
and appending the created Employee to the list.  The list of Employees is returned at the end of the method.
#### Parameters
- `file_name` (str): Name of the file to read from.
- `employee_data` (list): List of `Employee` objects to be filled with employee file data.
- `employee_type` (Employee): A reference to the `Employee` class.
#### Error Handling
- `FileNotFoundError`: Will create a blank list and create the file if the file can't be located
- `JSONDecodeError`: Will clear and reset JSON file if it gets corrupted
- `Exception`: If there is a non-specific error.
#### Returns
- `list`: List of `Employee` objects.


#### 2.) Write Employee File Method
`write_employee_data_to_file(file_name: str, employee_data: list) -> None`
#### Code Example
```python
    def write_employee_data_to_file(file_name: str, employee_data: list):
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
```
#### Description
- This function takes a list of `Employee` objects and converts it to a list of dictionaries. The dictionaries are then 
saved to a JSON file.  Similar to reading you will use a `for loop` to iterate of the Employee object list and create 
a list of dictionaries.  This is needed due to the specific syntax requirements for the JSON storage file
#### Parameters
- `file_name` (str): Name of the file to write to.
- `employee_data` (list): List of `Employee` objects.
#### Error Handling
- `TypeError`: If the data is not in a valid JSON format.
- `PermissionError`: If there is an issue with the data file's read/write permission.
- `Exception`: If there is a non-specific error.
#### Returns
- `None`


### How to use the processing_classes.py file
1. Import the modules/classes that `FileProcessor` class utilizes:
    ```python
    from data_classes import Employee
    from presentation_classes import IO
    import json
    ```
2. Create an instance of the `FileProcessor` class and use its methods as needed.
    ```python
    # Example usage
    processor = FileProcessor()
    employees = processor.read_employee_data_from_file(file_name='EmployeeRatings.json', employee_data=[], employee_type=Employee)
    processor.write_employee_data_to_file(file_name='EmployeeRatings.json', employee_data=employees)
    ```
# File -> (presentation_classes.py)
This is the presentation class Python file for the Employee Review Application. It includes the `IO` class, which provides functions for managing user input and output.

## IO Class
### Description
A collection of presentation layer methods that manage user input and output.  This class will handle outputting stored
user data, collecting new employee data, outputting error messages, outputting menu options, and finally collecting user
input for navigation of the application
### Methods
#### 1.) Output Error Message Function
#### `output_error_messages(message: str, error: Exception = None) -> None`
#### Code Example
```python
    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        try:
            print(message, end="\n\n")
            if error is not None:
                print(message)
                print(error, error.__doc__, type(error), sep='\n')
        except Exception as e:
            IO.output_error_messages(e.__str__())
```
#### Description
- Displays custom error messages to the user.  This method takes in a custom message for a specific error and then outputs
the message along with detailed information in regard to the type of error.
#### Parameters
- `message` (str): Message data to display in regards to the specific error.
- `error` (Exception): Exception object with technical message to display.
#### Error Handling
- `Exception`: If there is a non-specific error.
#### Returns
- `None`

#### 2.) Output Menu Function
#### `output_menu(menu: str) -> None`
#### Code Example
```python
   @staticmethod
    def output_menu(menu: str):
        try:
            print()
            print(menu)
            print()
        except Exception as e:
            IO.output_error_messages(e.__str__())
```
#### Description
- Displays the menu of choices to the user.
#### Parameters
- `menu` (str): Menu options string.
#### Error Handling
- `Exception`: If there is a non-specific error.
#### Returns
- `None`

#### 3.) Input Menu Choice Function
#### `input_menu_choice() -> str`
#### Code Example
```python
    @staticmethod
    def input_menu_choice():
        # Resets choice to zero then collects new input.  If not 1-4 it will raise an exception.
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # passing the exception object to avoid the technical message

        return choice
```
#### Description
- Gets a menu choice from the user ranging from 1-4.  If the user inputs anything other than 1-4 it will raise an
exception prompting the user to choose another option.
#### Error Handling
- `Exception`: If there is a non-specific error.
#### Returns
- `str`: User's menu choice.

#### 4.) Output Employee Data Function
#### `output_employee_data(employee_data: list) -> None`
#### Code Example
```python
  @staticmethod
    def output_employee_data(employee_data: list):
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
```
#### Description
- Displays employee data to the user.  Takes in the currently stored list of employees then using a `for loop` iterates
over the list using a curated `.foramt()` string to output a custom message based on the current students `review_rating`.  
Will print out each `Employee` til it gets to the end.

#### Parameters
- `employee_data` (list): List of employee object data to be displayed.
#### Error Handling
- `Exception`: If there is a non-specific error.
#### Returns
- `None`

#### 5.) Input Employee Data Function
#### `input_employee_data(employee_data: list, employee_type: Employee) -> list`
#### Code Example
```python
   @staticmethod
    def input_employee_data(employee_data: list, employee_type: Employee):
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
```
#### Description
- Collects the first name, last name, review date, and review rating for the employee error handling for invalid input
is handled in the Employee and Persons class getters and setters.  Additional error handling is utilized to capture data
outside of the ordinary.
#### Parameters
- `employee_data` (list): List of Employee data to be filled with input data.
- `employee_type` (Employee): A reference to the `Employee` class.
#### Error Handling
- `ValueError`: Handles Value errors that are out of scope of the classes setters
- `Exception`: If there is a non-specific error.
#### Returns
- `list`: Updated list of employee data.

# Unit Testing
The employee rating program also comes with three unit test files that test out all the satellite files of the main file.
The unit test files include:

- `test_data_classes.py`
- `test_processing_classes.py`
- `test_presentation_classes.py`

I will cover each of the test files and their corresponding tests and the logic behind them.

## File -> (test_data_classes.py)

### Description
This unit test file, test_data_classes.py, is designed to validate the functionality of the data classes in the Employee 
Review Application, specifically the Person and Employee classes found in the data_classes.py file.

### Test PersonClass `class TestPerson(unittest.TestCase):`
#### 1. ) `test_person_init`
#### Code Example
```python
    def test_person_init(self):
        """
        Unit test to test the initializer of the Person Class

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        person = Person("Alex", "clark")
        self.assertEqual("Alex", person.first_name)
        self.assertEqual("Clark", person.last_name)
```
#### Description
- This test is used to test out the initializer of the Person class by creating a sample Person.  The attributes for
first and last name are then called and compared to the expected value.


#### 2. ) `test_person_invalid_first_name`
#### Code Example
```python
        def test_person_invalid_first_name(self):
        """
        Unit test to test the setter of the first_name property

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        with self.assertRaises(ValueError):
            person = Person("123", "clark")
```
#### Description
- This test is used to test out the setter for first name of the Person Class so that if a user inputs incorrect value
for first name it will raise a value error.  This test is done by creating an incorrect person and testing if the
correct error is raised.

#### 3. ) `test_person_invalid_last_name`
#### Code Example
```python
       def test_person_invalid_last_name(self):
        """
        Unit test to test the setter of the last_name property

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        with self.assertRaises(ValueError):
            person = Person("Alex", "123")
```
#### Description
- This test is used to test out the setter for last name of the Person Class so that if a user inputs incorrect value
for last name it will raise a value error.  This test is done by creating an incorrect person and testing if the
correct error is raised.

#### 4. ) `test_person_str`
#### Code Example
```python
    def test_person_str(self):
        """
        Unit test to test the str attribute of the Person Class

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        person = Person("alex", "clark")
        self.assertEqual("Alex,Clark", str(person))
```
#### Description
- Testing the string attribute by create a person and running the str command on it and comparing the expected value.

### Test EmployeeClass `class TestEmployee(unittest.TestCase):`
#### 1. ) `test_employee_init`
#### Code Example
```python
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
```
#### Description
- This test is used to test out the initializer of the Employee class by creating a sample Employee with correct values.  
The attributes for name,rating,and date are then called and compared to the expected sample value.

#### 2. ) `test_review_date_invalid_type`
#### Code Example
```python
    def test_review_date_invalid_type(self):
        """
        Unit test to test the setter of the review_data property

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        with self.assertRaises(ValueError):
            employee = Employee("alex", "clark", "05Jan2023", 3)
```
#### Description
- This test is used to test out the setter of the review date property.  A sample employee with the incorrect date 
format is created and the test checks to see if a ValueError is returned.

#### 3. ) `test_review_date_invalid_type`
#### Code Example
```python
    def test_review_rating_invalid_type(self):
        """
        Unit test to test the setter of the review_rating property

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        with self.assertRaises(ValueError):
            employee = Employee("alex", "clark", "05Jan2023", 3.3)
```
#### Description
- This test is used to test out the setter of the rating property.  A sample employee with the incorrect rating value 
format is created and the test checks to see if a ValueError is returned.

#### 4. ) `test_review_date_invalid_type`
#### Code Example
```python
    def test_employee_str(self):
        """
        Unit test to test the str attribute of the Employee Class

        ChangeLog: (Who, When, What)
        Alexander R. Clark, 10Dec2023: Created the test.
        """
        employee = Employee("alex", "clark", "2023-01-01", 3)
        self.assertEqual("Alex,Clark,2023-01-01,3", str(employee))

```
#### Description
- This test is used to test the str attribute of employee by creating a sample employee and comparing the expected value
to the `str(employee)` command.

## File -> (test_processing_classes.py)
### Description
This unit test file, test_processing_classes.py, is designed to validate the functionality of the processing classes in the Employee 
Review Application, specifically the FileProcessor class, which have a number of methods to validate

### Test FileProcessorClass `class TestFileProcessor(unittest.TestCase):`
#### 1. ) `test_read_employee_data_from_file`
#### Code Example
```python
    def setUp(self):
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file_name = self.temp_file.name
    def tearDown(self):
        pass
    
    def test_read_employee_data_from_file(self):
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
```
#### Description
- Unit Test to test the `read_employee_data_from_file` function.  A sample set of data is created to be writen to a temporary
        file.  The file is then read and stored in employees.  The sample set is then compared to the employees list
        to confirm it is the same length and that all values are equal in comparison by iterating over a `for loop`

#### 2. ) `test_read_employee_data_from_file_invalid_json`
#### Code Example
```python
    def test_read_employee_data_from_file_invalid_json(self):
        with open(self.temp_file_name, 'w') as file:
            file.write("invalid file")
        employees: list = []  # a table of employee data
        employees = FileProcessor.read_employee_data_from_file(file_name=self.temp_file_name, employee_data=employees,
                                                               employee_type=Employee)
        self.assertEqual(0, len(employees))
```
#### Description
- Unit Test to test the read_data_from_file function if an invalid JSON file is read.  A temp file is created in
        the wrong format and then read using the read_employee_data_from_file function.  When this function is ran this
        way the program should return a blank list resetting the file to [].  A test is ran to confirm the list len is
        0.

#### 3. ) `test_read_employee_data_from_file_file_not_found`
#### Code Example
```python
    def test_read_employee_data_from_file_file_not_found(self): 
        employees: list = []  # a table of employee data
        employees = FileProcessor.read_employee_data_from_file(file_name="name", employee_data=employees,
                                                               employee_type=Employee)
        self.assertEqual(0, len(employees))
```
#### Description
- Unit Test to test the read_data_from_file function if file is not found.  In this test the file name is modified
        to a name that will not be located and the employees list is checked on whether it's length is zero

#### 4. ) `test_write_employee_data_from_file`
#### Code Example
```python
    def test_write_employee_data_to_file(self):
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
```
#### Description
- Unit Test to test the write_employee_data_to_file function.  A sample set of a list of Employees is made
        to write to a temporary file.  The file is then read and loaded into file data.  The original sample data is
        then compared to the data in file_data to compare len and to ensure each value is the same on every
        iteration and keyword.

## File -> (test_presentation_classes.py)
### Description
This unit test file, test_presentation_classes.py, is designed to validate the functionality of the presentation classes
in the Employee Review Application, specifically the IO class, which have a number of methods that handle input and output

### Test IOClass `class TestIO(unittest.TestCase):`
#### 1. ) `test_input_menu_choice`
#### Code Example
```python
    def test_input_menu_choice(self):
        with patch("builtins.input", return_value="2"):
            choice = IO.input_menu_choice()
            self.assertEqual("2", choice)
```
#### Description
- Unit test to verify the input_menu_choice function is storing the appropriate value.  2 is patched to the function
 when the method is called and the return value is stored in choice. If choice is not 2 the test fails.

#### 2. ) `test_input_employee_data`
#### Code Example
```python
    def test_input_employee_data(self):
        with patch("builtins.input", side_effect=["Alex", "Clark", "2023-01-01", 5]):
            employees = []
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)
            self.assertEqual(1, len(employees))
            self.assertEqual("Alex", employees[0].first_name)
            self.assertEqual("Clark", employees[0].last_name)
            self.assertEqual("2023-01-01", employees[0].review_date)
            self.assertEqual(5, employees[0].review_rating)
```
#### Description
- Unit test to verify the input_employee_data function is storing the appropriate value.  It is patched a test
        sample then each value is tested against the expected value

#### 3. ) `test_input_employee_data_invalid_data`
#### Code Example
```python
    def test_input_employee_data_invalid_date(self):
        with patch("builtins.input", side_effect=["Alex", "Clark", "25343", 5]):
            employees = []
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)
            self.assertEqual(0, len(employees))
```
#### Description
- Unit test to verify the input_employee_data function will not store a value if incorrect data is entered.
        It is patched a test sample that has an error in the data value and will pass the test if the list is length 0,
since no item should be added to the list.

#### 4. ) `test_input_employee_data_invalid_rating`
#### Code Example
```python
    def test_input_employee_data_invalid_rating(self):
        with patch("builtins.input", side_effect=["Alex", "Clark", "2023-01-01", 6]):
            employees = []
            employees = IO.input_employee_data(employee_data=employees, employee_type=Employee)
            self.assertEqual(0, len(employees))
```
#### Description
- Unit test to verify the input_employee_data function will not store data if invalid rating is used.  The sample
        data is given a rating of 6 to test that when used the employee object is not created and list remains len 0

#### 5. ) `test_output_menu`
#### Code Example
```python
    def test_output_menu(self):
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
```
#### Description
-  Unit test to verify the format of the output menu is correct.  Tests the output_menu on a sample of the test
        MENU constant.  The output from the console is then stored in actual_output and tested against the curated
        string in the expected_output value.

#### 6. ) `test_output_menu`
#### Code Example
```python
    def test_output_employee_data(self):
        with patch("sys.stdout", new_callable=StringIO) as mock:
            employees =[Employee("Alex", "Clark", "2024-01-01", 5)]
            IO.output_employee_data(employee_data=employees)
        actual_output = mock.getvalue()
        expected_output = ("\n--------------------------------------------------\n Alex Clark is rated as 5 ("
                           "Leading)\n--------------------------------------------------\n\n")
        self.assertEqual(expected_output, actual_output)
```
#### Description
-  Unit test to verify the format of the output_employee_data function is correct. A sample list is created and
        passed to the output_employee_data function.  The output from the function is collected in actual_output and
        then compared to the expected_output string to ensure the format of the output is correct.