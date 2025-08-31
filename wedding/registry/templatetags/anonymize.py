
from django import template
from django.template.defaultfilters import stringfilter 

register = template.Library()
@register.filter
@stringfilter
def hide_name(value):
    all_words = value.split(' ')
    all_words = ' '.join([x[0] + (len(x) - 1)*'*' for x in all_words])
    return all_words

