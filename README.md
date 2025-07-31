# Employee Management System

A Django-based CRUD application for managing employee records with position assignments.

## Features

- **Employee Management**: Add, view, edit, and delete employee records
- **Position Management**: Manage job positions and assign them to employees
- **Employee Information**: Track full name, employee ID, email, position, and join date
- **Web Interface**: User-friendly HTML templates for all operations
- **Data Validation**: Form validation and unique email constraints

## Project Structure

```
employee_project/
├── employee_register/          # Main Django app
│   ├── models.py              # Employee and Position models
│   ├── views.py               # CRUD operations
│   ├── forms.py               # Django forms
│   ├── urls.py                # URL routing
│   └── templates/             # HTML templates
│       └── employee_register/
│           ├── base.html
│           ├── employee_form.html
│           └── employee_list.html
├── employee_project/          # Django project settings
├── manage.py                  # Django management script
└── db.sqlite3                # SQLite database
```

## Models

- **Employee**: Stores employee information (name, ID, email, position, join date)
- **Position**: Manages job positions with titles

## Usage

- **View Employees**: Browse all registered employees
- **Add Employee**: Create new employee records with position assignment
- **Edit Employee**: Update existing employee information
- **Delete Employee**: Remove employee records from the system
- **Manage Positions**: Add and manage job positions

## Technologies Used

- **Backend**: Django (Python)
- **Database**: SQLite
- **Frontend**: HTML templates with Django templating
- **Styling**: Basic HTML/CSS

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
