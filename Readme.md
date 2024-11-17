# Student Management System


1. Project Setup
Create a virtual environment:
```
python3 -m venv student_env
source student_env/bin/activate
```
start django
```
pip3 install django
django-admin startproject student_management

cd student_management
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

note:
```
Username (leave blank to use 'mingyang'): mingyang
Email address: zmyswufe@gmail.com
Password: mingyang
```

2. Added Student model in student_model app

```
python3 manage.py startapp students
```
Add 'students' to the INSTALLED_APPS list in the student_management/settings.py file.

```
python3 manage.py makemigrations
python3 manage.py migrate
```

3. Registered Student model in admin panel

4. Added views and templates

5. Added form validations for email and grade in StudentForm

6. Implemented user authentication and restricted access to student records

7. Added search functionality for student list by name

8. Implemented pagination for student list

9. Implemented error handling and validation