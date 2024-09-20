Here’s a merged version of your two Markdown files:

---

# Xtension Assignment

This repository contains the solutions for the Xtension Assignment.

## Project Structure

The project is organized into separate folders for each task. Each folder contains two files:
- A .py file with the Python code implementation
- A .md file with an explanation of the code

### To-Do List Application

This folder contains a Django-based To-Do List application, which is part of the Xtension assignment repository.

#### To-Do List Application Structure

```
To_Do_List_Application/
├── env/
├── To_Do_List/
│   ├── tasks/
│   │   ├── __pycache__/
│   │   ├── migrations/
│   │   ├── templates/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── To_Do_List/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── db.sqlite3
│   └── manage.py
```

## Getting Started

### Cloning the Repository

To get a local copy of this project, clone it using git:

```bash
git clone https://github.com/Gaganjeet15/Xtension_assignment.git
cd Xtension_assignment
```

### Installation

Most tasks can be run directly without any additional installation. However, for Task 12 (API Data Fetching), you'll need to install the requests library:

```bash
pip install requests
```

For the To-Do List application:

1. Navigate to the To-Do List application folder:
   ```bash
   cd path/to/Xtension_assignment/To_Do_List_Application
   ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     env\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source env/bin/activate
     ```

3. The virtual environment should already have the required packages installed. If you need to reinstall them, use:
   ```bash
   pip install -r requirements.txt
   ```

   Note: If `requirements.txt` doesn't exist, you can create it using:
   ```bash
   pip freeze > requirements.txt
   ```

### Database Setup

The SQLite database (`db.sqlite3`) is already included in the project. If you need to apply any new migrations or create a superuser, follow these steps:

1. Apply migrations:
   ```bash
   python manage.py migrate
   ```

2. (Optional) Create a superuser to access the Django admin interface:
   ```bash
   python manage.py createsuperuser
   ```

## Usage

To run a specific task:

1. Navigate to the task's folder.
2. Run the Python file using a Python interpreter, e.g.:
   ```bash
   python "Task_2 - Palindrome Checker\palindrome_checker.py"
   ```

## Running the Application

To start the development server for the To-Do List application:

1. Ensure you're in the directory containing `manage.py` (To_Do_List_Application/To_Do_List/).
2. Run the following command:
   ```bash
   python manage.py runserver
   ```
3. Open a web browser and go to `http://127.0.0.1:8000/` to access the application.

## Features

- View a list of all tasks
- Add new tasks
- Mark tasks as complete

## Dependencies

- Python 3.12.1
- requests library (for Task 12 only)

## Contributing

This project is an assignment and is not currently open for contributions.

## License

This project is for educational purposes as part of the Xtension assignment.
