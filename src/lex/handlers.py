"""
Handlers for lex's API resources.
"""
import sys
import traceback

import ujson
from tornado.web import RequestHandler
from tornado_cors import CorsMixin

from lex import settings
from lex.params import validate


class BaseHandler(CorsMixin, RequestHandler):
    """
    Base Handler, which provides:
    - Error handling
    - CORS (Cross-Origin Resource Sharing)
    """

    CORS_ORIGIN = "*"
    CORS_HEADERS = settings.CORS_HEADERS

    def _handle_request_exception(self, exception):
        if hasattr(exception, "status_code"):
            status = exception.status_code
            msg = exception.message
            self.send_error(status, message=msg)
        else:
            status = 500
            exc_info = sys.exc_info()
            msg = "<br>".join(traceback.format_exception(*exc_info))
            self.send_error(status, exec_info=exc_info, message=msg)

    def write_error(self, status_code, **kwargs):
        self.prepare()
        error_json = {"error": kwargs.get("message")}
        self.finish(error_json)


class HealthcheckHandler(RequestHandler):
    """
    Return "Atchim!" if service is running.
    """

    def get(self):
        self.write("Atchim!")


class NewsHandler(BaseHandler):
    """
    Return a list of recommendations provided the user of interest.
    """

    def post(self):
        params = ujson.loads(self.request.body)
        validate(params)
        recommendation_list = [
            {
                "documentId": 6116038798098712381,
                "score": 0.999
            },
            {
                "documentId": 6502978799245377158,
                "score": 0.666
            },
            {
                "documentId": 5412347350701788586,
                "score": 0.333
            }
        ]
        self.write(ujson.dumps(recommendation_list))
