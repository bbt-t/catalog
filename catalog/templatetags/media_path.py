from django import template
from django.conf import settings


register = template.Library()


@register.simple_tag
def media_path(image_name):
    no_img_pic_name = "images/no_image.webp"
    if not image_name:
        return f"{settings.MEDIA_URL}{no_img_pic_name}"

    return f"{settings.MEDIA_URL}{image_name}"
