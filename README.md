# Team 2 Final Project

# Team

- Justin Walker-Baden — Team Leader
- Joshua Stine
- Cliff Victor

## About

- Django app for creating and managing event flyers.

- project diagrams and planning are in the doc files.

## Setup

```bash

git clone https://github.com/Sahtorin/Team-2-Final.git
cd Team-2-Final
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
```

## Notes

- db migrations have not been run yet. Will be added when models are finished.

- migration once models.py is done is as follows:

```bash

python manage.py makemigrations
python manage.py migrate
```
