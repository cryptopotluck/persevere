from django import template
register = template.Library()

@register.filter(name='pagination_limit')
def pagination_limit(obj, current=1, limit=10):

    left = (limit / 2) + 1
    right = limit / 2
    total = len(obj)

    if limit % 2 == 0:
        right -= 1

    if current < left:
        return obj[:limit]
    if current > total - right:
        return obj[total-limit:]


    return obj[int(current-left):int(current+right)]
