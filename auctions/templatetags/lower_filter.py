from django import template 
  
register = template.Library() 
  
@register.filter() 
def low(value): 
    return value.lower()
