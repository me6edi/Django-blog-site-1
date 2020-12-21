from django import template

register = template.Library()

@register.filter(name='get_dict')
def get_val(dict, key):
    return dict[key]
