import djangoxmako
from django.conf import settings
from django.http import HttpResponse, HttpResponseServerError
from mako import exceptions

def render_to_response(filename, dictionary, context_instance=None):

    dictionary.update(djangoxmako.default_context)
    
    if context_instance:
        for context_dict in context_instance.dicts:
            dictionary.update(context_dict)
    
    if hasattr(settings, 'MAKO_DEFAULT_CONTEXT'):
        dictionary.update(settings.MAKO_DEFAULT_CONTEXT)

    try:
        template = djangoxmako.template_lookup.get_template(filename)
        return HttpResponse(template.render(**dictionary))
    except:
        return HttpResponseServerError(exceptions.html_error_template().render())
