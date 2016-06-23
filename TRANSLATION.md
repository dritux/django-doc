# Translation


### Alter polls/views.py
```
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext as _

def index(request):
    output = _("Welcome to my site.")

    return HttpResponse(output)
```
---
settings.py
```
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'django_translation/locale'),
)
```
---

### Generate templates

$ python manage.py makemessages -l es
$ python manage.py compilemessages -l


