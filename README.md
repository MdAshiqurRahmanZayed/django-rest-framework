# django-rest-framework



## Setup
The first thing to do is to clone the repository:


(For FunctionBased )

```sh
$ git clone https://github.com/MdAshiqurRahmanZayed/django-rest-framework.git
$ cd django-rest-framework/FunctionBased
```
Create a virtual environment to install dependencies in and activate it:
use python 3.8 / 3.9

```sh
$ virtualenv -p python3 env
$ source env/bin/activate
```
Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

we have to migrate
```sh
$ python manage.py makemigrations 
$ python manage.py migrate 
$ python manage.py createsuperuser
$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`

(For ClassBased )

```sh
$ git clone https://github.com/MdAshiqurRahmanZayed/django-rest-framework.git
$ cd django-rest-framework/ClassBased
```
Create a virtual environment to install dependencies in and activate it:
use python 3.8 / 3.9

```sh
$ virtualenv -p python3 env
$ source env/bin/activate
```
Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

we have to migrate
```sh
$ python manage.py makemigrations 
$ python manage.py migrate 
$ python manage.py createsuperuser
$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/`


