# drf-tutorial

<hr/>

-   Create env -> `python -m venv env `
-   Activate env -> `.\env\Scripts\activate`
-   Install required libraries

```
pip install django
pip install djangorestframework
pip install pygments
```

<hr>

-   Create new project `django-admin startproject tutorial1_serialization`
-   Create new app name `snippets` inside project

```
cd .\tutorial1_serialization\
python manage.py startapp snippets
```

-   Create an initial migration for our snippet model, and sync the database for the first time

```
python manage.py makemigrations snippets
python manage.py migrate snippets
```
