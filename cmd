virtualenv venv
source venv/bin/activate
django-admin startproject mysite .
python3 manage.py runserve
python3 manage.py startapp blog
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py shell

