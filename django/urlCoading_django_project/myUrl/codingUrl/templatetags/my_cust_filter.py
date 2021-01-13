from django import template

register = template.Library()
@register.filter(name='sep')
def myfun2(value,args):
    return value.replace(args,'kavya')