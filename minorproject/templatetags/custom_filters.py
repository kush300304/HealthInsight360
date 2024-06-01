
from django import template

register = template.Library()

@register.filter
def unique_items(input_list):
    return list(set(input_list))