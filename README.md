# hsgs-apicta

## Installation

Install the prerequisites:

    apt install git mariadb-server libmysqlclient-dev
    pip3 install virtualenv

Setup database for the server:

    mysql -uroot -p
    mariadb> CREATE DATABASE apicta DEFAULT CHARACTER SET utf8mb4 DEFAULT COLLATE utf8mb4_general_ci;
    mariadb> GRANT ALL PRIVILEGES ON apicta.* to 'dmoj'@'localhost' IDENTIFIED BY '<password>';
    mariadb> exit

Activate the virtual environment:
    virtualenv venv
    source venv/bin/activate

From this part, we are inside the virtual environment.

Clone this repository to your local machine:

    (venv) git clone https://github.com/hung3a8/hsgs-apicta.git
    (venv) cd hsgs-apicta

Inside the repository, start installing Python requirements:
    (venv) pip3 install -r requirements.txt

Now you will need to create new file `apicta/local_settings.py`. Here, you put down some private settings like you database settings (including your password), etc. This file is excluded from being tracked by git so feel free to put any settings there. `apicta/settings.py` will directly read settings from `apicta/local_settings.py`, but `Django` won't track it for reloading.

Now, you should verify that everything is working fine:

    (venv) python3 manage.py check

We need to collect static files into `STATIC_ROOT` as specified in the settings:

    (venv) python3 manage.py collectstatic

We must generate the schema for the database, since it is currently empty:

    (venv) python3 manage.py migrate

The database is currently empty. In the future, we will provide you some initial data for the server.

You should create an admin account with which to login initially.

    (venv) python3 manage.py createsuperuser

If after running server, you can't access the user detail page, then reapply the migration 0002.