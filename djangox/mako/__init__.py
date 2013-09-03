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
from django.core.urlresolvers import reverse, get_resolver, get_urlconf
from django.templatetags import static
from django.template import defaulttags
import types

def url(view_name, *args, **kwargs):
    try:
        return reverse(view_name, args=args, kwargs=kwargs)
    except:
        resolver = get_resolver(get_urlconf())
        for key in resolver.reverse_dict.keys():
            if isinstance(key, types.FunctionType):
                name = key.__module__ + '.' + key.__name__
            else:
                name = key
            
            if name.endswith(view_name):
                return reverse(name, args=args, kwargs=kwargs)
        
        raise
        

default_context = {
    'url' : url,
    'static': static.static
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
