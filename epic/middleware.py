import logging
from ast import literal_eval

from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger('main')


class LoggingMiddleware(MiddlewareMixin):
    """Log requests from users."""
    # def __init__(self, get_response):
    #     self.get_response = get_response
    #     # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        if request.method != 'GET':
            post = request.POST.copy()
            if 'password' in post:
                post.pop('password')

            if response['content-type'] == 'application/json':
                if getattr(response, 'streaming', False):
                    response_body = '<<<Streaming>>>'
                else:
                    response_body = literal_eval(response.content.decode('utf-8'))
            else:
                response_body = post

            logger.info('[POST] request by %s (id %s) from %s. Form content: %s', request.user,
                        request.user.id, resolve(request.path).url_name, response_body)

        return response
