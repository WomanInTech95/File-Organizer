File Organizer in Python

A simple command-line tool that organizes files in a specified directory by moving them into subfolders based on their file extensions.

Features

Automatically organizes files into subdirectories named after their extensions (e.g., .txt files go into a txt folder).
Skips any existing directories to avoid moving them.
Provides a simple command-line interface for user interaction.
Requirements

Python 3.x
Installation

Clone the repository (if applicable) or download the file_organizer.py file.
Ensure Python is installed on your system. You can download it from python.org.
Usage

Open a terminal (or command prompt).
Navigate to the directory where you saved the file_organizer.py file.
Run the script using the following command:
bash
Copy code
python file_organizer.py
When prompted, enter the path of the directory you want to organize. For example:
javascript
Copy code
Enter the path of the directory to organize: /path/to/your/directory
Example

If you have a directory with the following files:

bash
Copy code
/my_directory/
    ├── file1.txt
    ├── file2.jpg
    ├── file3.txt
    ├── file4.png
After running the file organizer, the directory will look like this:

bash
Copy code
/my_directory/
    ├── txt/
    │   ├── file1.txt
    │   └── file3.txt
    ├── jpg/
    │   └── file2.jpg
    └── png/
        └── file4.png
Notes

Ensure you have the necessary permissions to move files in the specified directory.
Test the script in a safe environment to confirm its functionality before using it on important data.
