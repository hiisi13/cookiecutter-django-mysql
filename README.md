cookiecutter-django-mysql
=========================

A cookiecutter template for creating Django projects using MySQL as database.

Inherits pretty much everything from [pydanny's cookiecutter-django](https://github.com/pydanny/cookiecutter-django), but uses MySQL instead of PostgreSQL and adds post gen hook.

Usage
=====

Create and activate a virtualenv.


Install (cookiecutter)[https://github.com/audreyr/cookiecutter]
```
pip install cookicutter
```

Run it against this repo:
```
cookiecutter https://github.com/hiisi13/cookiecutter-django-mysql.git
```

Cookiecutter prompts you for questions. Answer them.

### Post gen hook

Does a few things for you:

* Installs local requirements
* Creates MySQL database using {{cookiecutter.repo_name}} as database name
* Syncs db and runs migrations with corresponding Django commands
* Run Django's createsuperuser command which will prompt you for questions
