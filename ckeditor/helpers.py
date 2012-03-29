import jingo
from django.contrib.contenttypes.models import ContentType


@jingo.register.function
def object_url(content_type_id, id):
    try:
        content_type = ContentType.objects.get(id=content_type_id)
        model = content_type.model_class()
        content = model.objects.get(id=id)
        return content.get_absolute_url()
    except:
        return None