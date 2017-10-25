# django-survey
Simple Survey system using Django Framework.

### Features
  * Use of session keys and session variables.
  * Basic Django ORM functionality.
  * Django fixtures through JSON.
  * Default Django user login functionality.
  * Bootstrap templates with Jinja 2.
  * Use of Django admin templates.

### Dependancy
###### Django==1.11.3
###### mysqlclient==1.3.12

### MySQL Commands
```shell
mysql>mysql -u username -p
mysql>CREATE DATABASE surveydb;
```

### Modify settings.py USER and PASSWORD (default shown)

###### 'USER': 'root',
###### 'PASSWORD': 'admin'

### Migrate/Create Admin

```shell
dir/surveyapp>python manage.py makemigrations
dir/surveyapp>python manage.py migrate
dir/surveyapp>python manage.py createsuperuser
```

### Load Fixtures (Preloaded survey questions)
```shell
dir/surveyapp>python manage.py loaddata preload_data.json
```

### Run Server
```shell
dir/surveyapp>python manage.py runserver
```

### Information
###### Signing in as an admin will reissue another session key (restarting the survey process).
