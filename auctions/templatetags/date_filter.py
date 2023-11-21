from django import template 
from datetime import date
  
register = template.Library() 
  
@register.filter() 
def daysago(value): 
    delta = value.date() - date.today()
    if delta.days == 0:
        return "Today"
    else:
        return f"{abs(delta.days)} days ago"
