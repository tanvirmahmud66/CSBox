from django import template
from django.utils.timesince import timesince
from django.utils import timezone

register = template.Library()

@register.filter(name='format_time')
def format_time(value):
    if not value:
        return ''  # Return empty string for invalid or empty values

    if isinstance(value, str):
        try:
            value = timezone.datetime.strptime(value, "%Y-%m-%d %H:%M:%S")
        except ValueError:
            return ''  # Return empty string for invalid datetime strings

    time_diff = timezone.now() - value
    minutes = int(time_diff.total_seconds() / 60)
    hours = int(time_diff.total_seconds() / 3600)
    days = int(time_diff.total_seconds() / 86400)

    if days >= 4:
        return value.strftime('%Y-%m-%d')  # Show the created date if it's been 4 or more days
    elif hours >= 24:
        return f'{days} day{"s" if days != 1 else ""}'  # Show days when it's 1 day or more
    elif minutes >= 60:
        return f'{hours} hour{"s" if hours != 1 else ""}'  # Show hours when it's 1 hour or more
    else:
        return f'{minutes} minute{"s" if minutes != 1 else ""}'  # Show minutes otherwise
