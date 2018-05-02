### Prerequisites

The prerequisites for execute the project are postgreSql, django, djangorestframework and psycopg2.
Also is important migrate the tables to our database to do these we use the command:

```
$ python manage.py makemigrations
$ python manage.py migrate
```

NOTE: For this step is needed configure the login and name information of the database 


### Installing

To install the software needed is important have pip installed read https://pypi.python.org/pypi/pip:

```
$ pip install django djangorestframework psycopg2

```
For postgresql we can install it from https://www.postgresql.org/download/

## Creating Modules or Apss
The project consist of a set of modules or apps. In order to create a new module enter the following command.
```
$ python manage.py startapp sales
```
The fisrt time that the app is created, it has the following files


```
\sales
  \migrations
    __init__.py
  __init__.py
  admin.py
  apps.py
  models.py
  tests.py
  views.py
```

## Programming guideline for introduce code.


* The name of the modules is in plural and with lowercase

* The classes start with uppercase

* The functions start with lowercase

* If the function name consist on two words only the first start with lower case
```
Example: class salesList()
```
