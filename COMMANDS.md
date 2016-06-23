# commands

### Install django
```
sudo apt-get update
sudo apt-get install python-django
or
sudo pip install django
```

### Django get version
```
python -c "import django; print(django.get_version())"
or
django-admin --version
```

### Create new project 

$ django-admin startproject mysite

```

mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

### Create app

$ python manage.py startapp polls
```

polls/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```

### install bd
```
$ python manage.py migrate
```


### Write your first view
```
polls/views.py
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

### Create urls.py
```
polls/urls.py
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```

### Modify mysite url
```
mysite/urls.py
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
```








