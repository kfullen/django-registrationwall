from django import template

from .. import mixins
from .. import settings

register = template.Library()


@register.simple_tag(takes_context=True)
def get_regwall_attempts(context):
    request = context['request']
    try:
        return request.session['regwall']['attempts']
    except KeyError:
        return []


@register.simple_tag(takes_context=True)
def get_regwall_successes(context):
    request = context['request']
    try:
        return request.session['regwall']['successes']
    except KeyError:
        return []


@register.simple_tag
def get_regwall_limit():
    return settings.REGWALL_LIMIT


@register.simple_tag
def get_regwall_expire():
    return settings.REGWALL_EXPIRE
