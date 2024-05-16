from django.template.defaulttags import register
from .language import translator
import urllib.parse as urlparse

@register.filter(name='times') 
def times(number):
    return range(number)

@register.filter(name="t")
def translate(key, lang=None):
    return translator.t(key, lang=lang)

@register.filter(name="withlang")
def withlang(url, qlang=None):
    if qlang is not None:
        url_parts = list(urlparse.urlparse(url))
        query = dict(urlparse.parse_qsl(url_parts[4]))
        query.update({ "lang": qlang })
        url_parts[4] = urlparse.urlencode(query)
        return urlparse.urlunparse(url_parts)
    else:
        return url
