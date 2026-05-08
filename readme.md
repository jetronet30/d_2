
py -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

.venv\Scripts\activate

python.exe -m pip install --upgrade pip

pip install django

django-admin startproject project_name — ახალი პროექტის შექმნა
django-admin startapp app_name — ახალი app-ის შექმნა

py manage.py makemigrations

py manage.py migrate
py manage.py runserver


