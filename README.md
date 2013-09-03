# djangox-mako
django mako adapter

## template loader
Currently djangox-mako supports only app directories loader. You can put template file in your app directory's subdirectory named 'templates', djangox-mako can access that.

## usage
### render_to_response
	def someview(request):
	    ...
	    ...
        return render_to_response('dir/file.html', locals())
        
### render_to_response with RequestContext
	def someview(request):
	    ...
	    ...
        return render_to_response('dir/file.html', locals(), RequestContext(request))

With RequestContext, you can use context variables related to request, such as csrf_token.

### django template tags
#### url
django template

    {% url 'path.to.some_view' arg1=v1 arg2=v2 %}
    
djangox-mako

    ${url('path.to.some_view', v1, v2)}

#### csrf_token
django template
	
	{% csrf_token %}

The code above will be rendered as:

    <input type="hidden" name="csrfmiddlewaretoken" value="26ec0b9f301f077da66f7aa2d2ae11cd" />	
    
djangox-mako

    <input type="hidden" name="csrfmiddlewaretoken" value="${csrf_token}" />

and planning to make the code below possible. Not implemented yet.
    
    ${csrf_token_tag()}

#### static
django template

	{% static 'path/to/style.css' %}

djangox-mako

	${static('path/to/style.css')}

### encoding
Django settings variable DEFAULT_CHARSET will be used for input & output of templates. if None, 'utf8' will be default.

### default context
You can inject default context with django settings MAKO_DEFAULT_CONTEXT. It's dict type.

## Note
* Package name was changed at ver 1.0.2. djangoxmako -> djangox.mako. It uses python namesapce package.

## TODO
* consider necessity of django middleware. I don't think it's needed yet.
* csrf_token_tag()
* settings.TEMPLATE_DEBUG support
* render_to_string
* support filesystem loader (settings.TEMPLATE_DIR)
* any other feature that is supported by django template but not supported by djangox-mako.





