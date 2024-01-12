from django import template

register = template.Library()


@register.simple_tag()
def mediapath(photo):
    return f'/media/{photo}'
