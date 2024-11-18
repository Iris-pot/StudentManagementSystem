# Student Management System

This is a web-based application built with the Django framework for managing student information, grades, and other academic data.

## Features

	•	Student Management: Add, update, and delete student records.
	•	Grade Assignment: Assign grades between 1 and 12 to students.
	•	User Authentication: Secure login system for administrators.
	•	Responsive Design: User-friendly interface with responsive design.

## Prerequisites

	•	Python: Version 3.x
	•	Django: Version 3.x or higher
	•	Virtual Environment: Recommended for dependency management


## How to Start

1. Clone the Repository
```
git clone https://github.com/Mingyang096/StudentManagementSystem.git
cd StudentManagementSystem
```

2. Create a virtual environment
```
python3 -m venv student_env
source student_env/bin/activate
```

3. Install Dependencies
```
pip install -r requirements.txt
```

4. Apply Migrations

```
python3 manage.py migrate
```

5. Create a Superuser

```
python manage.py createsuperuser
```
When prompted, enter the following details:

	•	Username
	•	Email address
	•	Password

## How to Run Locally

Run the application locally by executing:
```
python3 manage.py runserver
```

Then navigate to:
```
http://127.0.0.1:8000/admin/
```
Use your admin credentials to log in. Then you can access the Django admin panel to manage students and other models.
