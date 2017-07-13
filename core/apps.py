from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

class SubDomainLanguageMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            subdomain = request.META['HTTP_HOST'].split('.')[0]
        except KeyError:
            subdomain = None

        if subdomain == 'en':
            request.session['django_language'] = 'en'
            request.LANGUAGE_CODE = 'en'
        else:
            request.session['django_language'] = 'cn'
            request.LANGUAGE_CODE = 'cn'

        return self.get_response(request)
