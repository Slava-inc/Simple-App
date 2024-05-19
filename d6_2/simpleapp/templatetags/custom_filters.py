from django import template


register = template.Library()

CURRENCIES_SYMBOLS = {
   'rub': 'Р',
   'usd': '$',
}

# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter() # в аргументе декоратора name можно указать имя фильтре. По умолчанию имя фильтра имя функции currency
def currency(value, code='rub'):
   """
   value: значение, к которому нужно применить фильтр
   """
   postfix = CURRENCIES_SYMBOLS[code]
   # Возвращаемое функцией значение подставится в шаблон.
   return f'{value} {postfix}'

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()

