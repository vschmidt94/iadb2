from django import template

register = template.Library()

@register.filter
def keyvalue(a_dict, key):
    '''
    Custom template filter. Provided a dictionary of values and a key, 
    lookup the key in the dictionary and return a (possibly sanitized)
    version of the dict value.
    '''
    try:
        value = getattr(a_dict, key)
    except AttributeError:
        value = None

    if type(value)==bool:
        # If value is boolean, return the string version for human readability
        value = str(value)
    elif value is None:
        # Don't show 'None' in the table if there is no value, just use empty space
        value = ' '
    elif(a_dict._meta.verbose_name == 'Requirement'):
        # Special handling for handling requirements
        # Hacky, but works until I figure out how to lookup the thing
        if value is 'S':
            value = 'Self'
        elif value is 'P':
            value = 'Parent'
        elif value is 'C':
            value = 'Children'

    return value