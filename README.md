# Student Management System

### A Python CLI application for managing student records

A Python command-line student management system created as a final assessment
project for the SYEMEN CAREERS Python course.

## Features

- Login protection with three attempts
- Add, view, update, and delete student records
- Search students by ID or name
- Filter students by course
- Rank students by grade
- Display global and course statistics
- Persist student data in a local text file
- Validate names, ages, IDs, courses, and grades

## Skills demonstrated

- Python fundamentals: variables, conditions, loops, functions, and collections
- Object-oriented programming with a `Student` class
- Designing an interactive command-line menu
- Reading and writing structured data with file handling
- Input validation and error handling with `try`/`except`
- Searching, filtering, sorting, and aggregating records
- Creating reusable functions and organizing application logic
- Applying basic authentication and limiting login attempts

## Technologies used

- **Python 3** - application language
- **Python standard library** - console input/output and file handling
- **Plain-text CSV-style storage** - local persistence in `students_data.txt`
- **Command-line interface (CLI)** - menu-based user interaction
- **Git** - source-control workflow

## Project structure

```text
Student-System/
├── app.py             # Application entry point and all management features
├── README.md          # Project documentation and usage guide
├── LICENSE            # MIT license
└── students_data.txt  # Runtime data file, created automatically
```

### Application internals

The main application flow is organized around these responsibilities:

- **Authentication** - validates the login credentials before opening the system
- **Data management** - loads, saves, clears, and persists student records
- **`Student` model** - represents a student and determines pass/fail status
- **Student operations** - adds, searches, updates, and deletes records
- **Analysis** - calculates rankings, global statistics, and course statistics
- **Menu loop** - connects user choices to the appropriate operation

## Requirements

- Python 3.8 or later
- No third-party packages are required

## Getting started

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the application:

   ```bash
   python app.py
   ```

   On Windows, you can also use:

   ```powershell
   py app.py
   ```

4. Sign in with the default credentials:

   | Field | Value |
   | --- | --- |
   | Username | `marwan` |
   | Password | `elmoghazy` |

## Main menu

After signing in, choose an option from the interactive menu:

1. Add a student
2. Show all students
3. Search by ID
4. Search by name
5. Update student data
6. Delete a student
7. Show global statistics
8. Show course statistics
9. Filter by course
10. Rank students by grade
11. Exit

## Data storage

The application stores records in `students_data.txt` in the current working
directory. If the file does not exist when the application starts, it creates
an empty file automatically.

Each record is stored as comma-separated values in this order:

```text
student_id,name,age,course,grade
```

The data file is updated automatically after adding, updating, or deleting a
student. Do not include commas in student names or course names because commas
are used as field separators.

## License

This project is distributed under the [MIT License](LICENSE).
