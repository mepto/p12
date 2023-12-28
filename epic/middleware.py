import logging

from django.urls import resolve
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger('main')


class LoggingMiddleware(MiddlewareMixin):
    """Log requests from users."""

    def __call__(self, request):
        """Call middleware at each reaquest and log non-GET request types."""
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        response = self.get_response(request)
        if request.method != 'GET':
            post = request.POST.copy()
            if 'password' in post:
                post.pop('password')

            if response['content-type'] == 'application/json':
                response_body = response.content.decode('utf-8')
            else:
                response_body = post

            logger.info('[%s] request by %s (id %s) from %s. Form content: %s',
                        request.method, request.user, request.user.id,
                        resolve(request.path).url_name, response_body)

        return response
