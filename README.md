# expense_tracker
Developed as a part of HubSpot assessment

### Initializing a virtual environment
    python3 -m venv <virtualEnvironmentName>

### Activating the virtual environment
    source <virtualEnvironmentName>/bin/activate

### Install Django
    python3 -m pip install Django 

### Starting a Django project
    django-admin startproject expense_tracker

### Creating an app inside the project
    cd expense_tracker
    python manage.py startapp expenses

##### Add the app to the INSTALLED_APPS in settings.py (expenses_tracker)
##### Migrate all the changes
    python manage.py migrate
##### Run the server
    python manage.py runserver
