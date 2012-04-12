import jingo
import jinja2
from django.contrib.contenttypes.models import ContentType
import re

@jingo.register.function
def object_url(content_type_id, id):
    try:
        content_type = ContentType.objects.get(id=content_type_id)
        model = content_type.model_class()
        content = model.objects.get(id=id)
        return content.get_absolute_url()
    except:
        return None


_object_url_regex = '\[\[\s*object_url\(\s*(\d+)\s*,\s*(\d+)\s*\)\s*\]\]'

def _replace_urls(match):
    try:
        content_type = ContentType.objects.get(id=match.groups()[0])
        model = content_type.model_class()
        content = model.objects.get(id=match.groups()[1])
        new_substr = content.get_absolute_url()
    except:
        new_substr = ''
    return new_substr


@jingo.register.filter
def render_urls(text):
    return jinja2.Markup(re.sub(_object_url_regex, _replace_urls, text))