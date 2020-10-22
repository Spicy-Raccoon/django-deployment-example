from django import template

register = template.Library()

def cuut(value,arg):
    '''
    Cuts out all values of "arg" from the string
    '''
    return value.replace(arg,'')

register.filter('cuut',cuut)
