from django import template
from django.core.urlresolvers import reverse
from django.conf import settings

register = template.Library()

@register.simple_tag
def navactive_complex(request, urls, slug):
    if slug in request.path_info:
        return "active"
    
    return ""

@register.simple_tag
def navactive(request, urls):
    return_value = ""
    if request.path in ( reverse(url) for url in urls.split() ):
        return_value = "active"    
    elif urls in request.path_info:
        return_value = "active"    

    return return_value


@register.tag
def settings_value(parser, token):
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, var = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError, "%r tag requires a single argument" % token.contents.split()[0]
    return SettingsValue(var)

class SettingsValue(template.Node):
    def __init__(self, var):
        self.arg = template.Variable(var)
    def render(self, context):
        return settings.__getattr__(str(self.arg))
