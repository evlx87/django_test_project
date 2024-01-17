from django import template
from django.db.models.fields.files import FieldFile


register = template.Library()


@register.simple_tag
@register.filter()
def mediapath(data: FieldFile) -> str:
    return data.url if data else '#'
