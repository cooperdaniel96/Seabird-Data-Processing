import pandas as pd
import tkinter as tk
from tkinter import filedialog

"""
This code defines a `DataSeriesCapture` class that extends the built-in list class and provides methods for adding data, performing binary searches, 
and calculating the number of integers between two target values in a sorted list. It also includes a method to read data from a CSV file 
and a graphical user interface (GUI) using the tkinter library. The GUI allows users to select a CSV file, enter column names and target values, 
and process the data. The code is followed by commented-out debugging sections that demonstrate the usage of the `DataSeriesCapture` class. 
Overall, this code provides a solution for capturing and processing data, as well as a user interface for ease of use.
"""

class DataSeriesCapture(list):
    """A class for capturing and processing a series of data."""

    # override init method to initialize the object with the given arguments'
    def __init__(self, *args):
        """
        Initialize the DataSeriesCapture object.

        Args:
            *args: Variable length arguments passed to the list class.
                Each argument is added as an element in the DataSeriesCapture object.
                If no arguments are provided, the DataSeriesCapture object is initialized as an empty list.
        """
        # argument is passed to the list class using super()
        if args:
            super().__init__(args)

    def build_stats(self, stats_attribute=None):
        """
        Build a statistics class based on the captured data.

        Args:
            stats_attribute (str, optional): The attribute used for statistics calculation.
                Defaults to None if not provided.

        Returns:
            Stats: A dynamically created class inheriting from DataSeriesCapture,
                   with additional attributes for statistics calculations.
        """
        # stats_attribute=None to satisfy:
        # stats = capture.build_stats()

        # DataSeriesCapture_class = self.__class__
        # Instead of using DataSeriesCapture_class as the base class, it should use self.__class__.

        # attributes dictionary is defined with stats attribute argument
        attributes = {
            'stats_attribute': stats_attribute
        }

        # cast each element to a float and sort it numerically
        self.sort(key=float)

        # use the type() function to dynamically create the child class
        return type('Stats', (self.__class__,), attributes)(*self)

    def add(self, num):
        """
        Add a number to the data capture.

        Args:
            num (int): The number to add to the data capture.

        Raises:
            TypeError: If the provided number is not an integer.
        """

        # check to see if element being added is an integer
        # add element to list if it is an integer
        if isinstance(num, int):
            self.append(num)
        else:
            raise TypeError("Only integers can be added to the list.")

    def between(self, target1, target2):
        """
        Calculate the quantity of elements between two targets in the captured data.

        Args:
            target1 (float): The first target value.
            target2 (float): The second target value.

        Returns:
            int: The quantity of elements between target1 and target2, including duplicates.
        """

        # use binary search to find the first and last occurence of our target
        first_target1_index = self.find_first_occurrence(target1)
        last_target2_index = self.find_last_occurrence(target2)

        # Count the integers between target1 and target2, including duplicates,
        # adding 1 to account for first index which is 0
        count = last_target2_index - first_target1_index + 1
        return count

    def find_first_occurrence(self, target):
        """
        Perform a binary search to find the index of the first occurrence of a target.

        Args:
            target (float): The target value to search for.

        Returns:
            int: The index of the first occurrence of the target.

        Notes:
            This function assumes the list is numerically sorted.
        """

        left = 0
        right = len(self) - 1
        # start indexing at -1 so that if no target is found, we will insert the index
        first_target_index = -1

        while left <= right:
            # checking if element at index mid is equal to target
            mid = (left + right) // 2
            if self[mid] == target:
                # Update target index with first occurrence index
                first_target_index = mid
                # In case of duplicates, look for the first occurrence to the left
                right = mid - 1
            # narrow down the search space to the right half of the current search range
            elif self[mid] < target:
                left = mid + 1
            # narrow down the search space to the left half of the current search range
            else:
                right = mid - 1

        # If target1 doesn't exist, place it at the left target index
        if first_target_index == -1:
            first_target_index = left

        return first_target_index

    def find_last_occurrence(self, target):
        """
        Perform a binary search to find the index of the last occurrence of a target.

        Args:
            target (float): The target value to search for.

        Returns:
            int: The index of the last occurrence of the target.

        Notes:
            This function assumes the list is numerically sorted.
        """
        left = 0
        right = len(self) - 1
        # start indexing at -1 so that if no target is found, we will insert the index
        last_target_index = -1

        while left <= right:
            # checking if element at index mid is equal to target
            mid = (left + right) // 2
            if self[mid] == target:
                # Update target index with the index of the last occurrence
                last_target_index = mid
                # Look for the last occurrence to the right
                left = mid + 1
            # narrow down the search space to the right half of the current search range
            elif self[mid] < target:
                left = mid + 1
            # narrow down the search space to the left half of the current search range
            else:
                right = mid - 1

        # If target2 doesn't exist, place it at the right target index
        if last_target_index == -1:
            last_target_index = right

        return last_target_index


    def read_pressure_from_csv(self, csv_name, header_name):
        """
        Read pressure data from a CSV file and add it to the data capture.

        Args:
            csv_name (str): The file path of the CSV file.
            header_name (str): The name of the header/column containing the data.
        """

        # seperate by semicolon and header starts on the second row
        # This assumes ';' is the separator, this should be changed
        # so that its configurable and more flexible when handling different formats
        try:
            df = pd.read_csv(csv_name, sep=';', header=1)
        except FileNotFoundError:
            print("Error: CSV file not found")
            return


        # Access and manipulate the DataFrame with the split columns
        # print(df)

        # Specify the column name
        column_name = header_name

        # Return the column as a pandas Series
        column = df[column_name]

        # Drop the second row of the series, which is the unit
        # This could be changed for flexibility as well
        column = column.iloc[1:]

        # Access and manipulate the column data
        # print(column)

        # Convert the Series to a list
        series_list = column.tolist()
        # Convert the list of strings to a list of floats
        float_list = [float(element) for element in series_list]

        # Extend the DataSeriesCapture object with the float_list
        self.extend(float_list)

class GUI:
    """A graphical user interface for CSV data processing."""

    def __init__(self):
        """
        Initialize the GUI window and its components.
        """

        # Create a GUI window
        self.window = tk.Tk()

        # Set the title and dimensions of the window
        self.window.title("CSV Data Processing")
        self.window.geometry("400x350")

        # Create a label for the "Select CSV File" prompt and display it in the window
        self.file_label = tk.Label(self.window, text="Select CSV File:")
        self.file_label.pack()

        # Create an entry field for the file path and display it in the window
        self.file_entry = tk.Entry(self.window, width=40)
        self.file_entry.pack()

        # Create a "Browse" button and display it in the window, linking it to the browse_file function
        self.browse_button = tk.Button(self.window, text="Browse", command=self.browse_file)
        self.browse_button.pack()

        # Create a label for the "Enter Column Name" prompt and display it in the window
        self.column_label = tk.Label(self.window, text="Enter Column Name:")
        self.column_label.pack()

        # Create an entry field for the column name and display it in the window
        self.column_entry = tk.Entry(self.window, width=30)
        self.column_entry.pack()

        # Create a label for the "Enter Target 1" prompt and display it in the window
        self.target1_label = tk.Label(self.window, text="Enter Target 1:")
        self.target1_label.pack()

        # Create an entry field for the first target value and display it in the window
        self.target1_entry = tk.Entry(self.window, width=10)
        self.target1_entry.pack()

        # Create a label for the "Enter Target 2" prompt and display it in the window
        self.target2_label = tk.Label(self.window, text="Enter Target 2:")
        self.target2_label.pack()

        # Create an entry field for the second target value and display it in the window
        self.target2_entry = tk.Entry(self.window, width=10)
        self.target2_entry.pack()

        # Create a "Process Data" button and display it in the window, linking it to the process_data function
        self.process_button = tk.Button(self.window, text="Process Data", command=self.process_data)
        self.process_button.pack()

        # Create a label for displaying the result and display it in the window
        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

        # Start the event loop to handle user interaction with the GUI
        self.window.mainloop()

    def browse_file(self):
        """
        Open a file dialog to allow the user to select a CSV file.
        """
        filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        # Clear the existing content in the file_entry widget
        self.file_entry.delete(0, tk.END)
        # Insert the selected file path into the file_entry widget
        self.file_entry.insert(0, filepath)

    def process_data(self):
        """
        Process the data based on the user's input.
        """
        # Get the content of the file_entry widget, which represents the selected file path
        filepath = self.file_entry.get()
        # Get the content of the column_entry widget, which represents the desired column name
        column = self.column_entry.get()
        # Get the content of the target1_entry widget, which represents the first target value
        target1 = self.target1_entry.get()
        # Get the content of the target2_entry widget, which represents the second target value
        target2 = self.target2_entry.get()

        # check for invalid inputs
        if not filepath or not column or not target1 or not target2:
            # Check if any of the required fields are empty or not provided
            self.result_label.config(text="Please enter all the required fields.")
            return

        try:
            # Attempt to convert the target1 and target2 values to floats
            target1 = float(target1)
            target2 = float(target2)
        except ValueError:
            # If the conversion to float fails, it means the provided values are not valid floats
            self.result_label.config(text="Please enter valid floats for targets.")
            return

        # Validate if target1 is smaller than target2
        if target1 >= target2:
            self.result_label.config(text="Target 1 should be smaller than Target 2.")
            return

        # Create an instance of the DataSeriesCapture class
        capture = DataSeriesCapture()
        try:
            # Read pressure data from the CSV file based on the provided file path and column name
            capture.read_pressure_from_csv(filepath, column)

            # Build stats for the captured data
            stats = capture.build_stats()
            # stats = capture.build_stats(capture)

            # Calculate the number of elements in the data list between the target values
            find_between = stats.between(target1, target2)

            # Update the result label with the calculated value
            self.result_label.config(text="Quantity of numbers between the targets: " + str(find_between))
        except FileNotFoundError:
            # Handle the case where the CSV file is not found
            self.result_label.config(text="CSV file not found.")
        except KeyError:
            # Handle the case where the provided column name is invalid
            self.result_label.config(text="Invalid column name.")


if __name__ == "__main__":
    gui = GUI()


    """
    Debugging PART1 and PART2
    
    PART1   
    # creating instance of DataSeriesCapture()
    capture = DataSeriesCapture()
    # add integers
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    # print(capture)

    # build stats
    stats = capture.build_stats(capture)
    # print(stats)

    # return how many numbers in the list are within a range
    start_target = 3
    end_target = 6
    find_between = stats.between(start_target, end_target)
    print('List between: ' + str(find_between))

    # child class
    print('Child list: ' + str(stats))
    # parent class
    print('Parent list: ' + str(capture))
    
    
    PART2
    capture2 = DataSeriesCapture()
    capture2.read_pressure_from_csv('58220.csv', 'PRESSION')
    # print(capture2)
    stats = capture2.build_stats(capture2)

    start_target = -2000
    end_target = 2000
    find_between = stats.between(start_target, end_target)
    # print(stats)
    print('List between: ' + str(find_between))
    """