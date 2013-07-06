from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.http import HttpResponse, HttpResponseServerError
from django.utils.importlib import import_module
from mako.lookup import TemplateLookup
from mako.template import Template
from mako import exceptions
import os
import sys
from django.template.defaulttags import URLNode, csrf_token
from django.core.urlresolvers import reverse
from django.conf import settings

default_context = {
    'url' : reverse,
}

default_charset = getattr(settings, 'DEFAULT_CHARSET', 'utf8')

app_template_dirs = []
fs_encoding = sys.getfilesystemencoding() or sys.getdefaultencoding()

for app in settings.INSTALLED_APPS:
    try:
        mod = import_module(app)
    except ImportError, e:
        raise ImproperlyConfigured('ImportError %s: %s' % (app, e.args[0]))
    template_dir = os.path.join(os.path.dirname(mod.__file__), 'templates')
    if os.path.isdir(template_dir):
        app_template_dirs.append(template_dir.decode(fs_encoding))


template_lookup = TemplateLookup(directories=app_template_dirs, 
                                 input_encoding=default_charset, 
                                 output_encoding=default_charset, 
                                 )
