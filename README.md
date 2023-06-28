# Seabird-Data-Processing

CSV Data Processing

Summary:
This program is designed to process data from a CSV file and perform calculations on a specific column of floats. 
It allows you to select a CSV file, specify the column name, and provide two target values. 
The program will then calculate the number of elements between the two targets in the selected column.

Instructions:

**Note: This script requires Python (version 3.6 or higher) to be installed on your computer.**

1. **Installation**

    - Install Python: If you don't have Python installed, download and install the latest version from the official Python website: https://www.python.org/downloads/

    - Install Required Libraries: Open a terminal or command prompt and execute the following command to install the necessary libraries:
    
        ```
        pip install pandas 
	pip install tkinter
        ```

2. **Download and Save the Script**

    - Download the provided script and save it to your desired location. 

3. **Execute the Script**

    - Open a terminal or command prompt.
    
    - Navigate to the directory where the script is saved using the `cd` command. For example:
    
        ```
        cd C:\path\to\script\directory
        ```

    - Run the script by executing the following command:
    
        ```
        python data_processing.py
        ```

4. **Graphical User Interface (GUI) Usage**

    - The script will open a GUI window.

    - Click the "Browse" button to select a CSV file. A file dialog will appear, allowing you to navigate to the desired CSV file and select it.

    - Enter the name of the column you want to process in the "Enter Column Name" field. Make sure to provide the exact column name as it appears in the CSV file.

    - Enter the first target value (a floating-point number) in the "Enter Target 1" field.

    - Enter the second target value (a floating-point number) in the "Enter Target 2" field.

    - Click the "Process Data" button to start the data processing.

    - The script will read the specified column from the CSV file, calculate the number of elements between the target values, and display the result in the GUI window.

    - If any of the required fields are empty or if the entered values are invalid, appropriate error messages will be displayed in the GUI window.

5. **Additional Notes**

    - If you encounter any issues or errors, please make sure you have followed the above steps correctly and that your CSV file is properly formatted.
