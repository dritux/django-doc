# Translation


### Update views file

polls/views.py
```
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import ugettext as _

def index(request):
    output = _("Welcome to my site.")

    return HttpResponse(output)
```
---

### Insert locale path

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
```
$ python manage.py makemessages -l es
$ python manage.py compilemessages -l
```

### Others settings.py
```
LANGUAGE_CODE = 'en-us'
USE_I18N = True 
USE_L10N = True

TEMPLATE_CONTEXT_PROCESSOR = ('django.core.context_processors.i18n',)

"django.middleware.locale.LocaleMiddleware", in MIDDLEWARE_CLASSES
```












