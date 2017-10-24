# django-survey
Simple Survey system using Django Framework

### Dependancy
###### Django==1.11.3
###### mysqlclient==1.3.12

### Terminal
```shell
mysql>mysql -u username -p
mysql>CREATE DATABASE surveydb;
```

### Modify settings.py USER and PASSWORD (default shown)

###### 'USER': 'root',
###### 'PASSWORD': 'admin'

### Migrate Data/Create Admin

```shell
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
