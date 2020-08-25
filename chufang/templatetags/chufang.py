from django import template
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def mark_unknown_prt_abbreviation(seq=''):

    return format_html(seq.replace('X', '<b style="color: red">X</b>'))
