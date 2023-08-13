from django import template
from django.conf import settings


register = template.Library()


@register.simple_tag
def media_path(image_name):
    return f"{settings.MEDIA_URL}{image_name}"
