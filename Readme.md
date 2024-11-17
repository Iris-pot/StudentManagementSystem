# Student Management System

## Project Setup
1. Create a virtual environment:
```
python3 -m venv student_env
source student_env/bin/activate
```
2. start django
```
pip3 install django
django-admin startproject student_management

cd student_management
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

note:
Username (leave blank to use 'mingyang'): mingyang
Email address: zmyswufe@gmail.com
Password: mingyang


