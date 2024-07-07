# api/middleware.py

from django.utils.deprecation import MiddlewareMixin
from django.core.cache import cache

class RequestCounterMiddleware(MiddlewareMixin):
    def process_request(self, request):
        count = cache.get('request_count', 0)
        cache.set('request_count', count + 1, None)
