"""
Handlers for lex's API resources.
"""
import ujson
from tornado.web import RequestHandler


class HealthcheckHandler(RequestHandler):
    """
    Return "Atchim!" if service is running.
    """

    def get(self):
        self.write("Atchim!")


class NewsHandler(RequestHandler):
    """
    Return a list of recommendations provided the user of interest.
    """

    def post(self):
        #params = ujson.loads(self.request.body)
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
