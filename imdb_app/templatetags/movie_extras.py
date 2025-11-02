from django import template
import math

register = template.Library()

@register.filter
def seconds_to_hm(value):
    if not value:
        return "N/A"
    hours = value // 3600
    minutes = (value % 3600) // 60
    if hours > 0:
        return f"{hours}h {minutes}m"
    return f"{minutes}m"