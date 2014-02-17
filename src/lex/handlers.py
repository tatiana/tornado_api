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
        recommendation_list = [
            {
                "documentId": "1233",
                "score": 0.999
            },
            {
                "documentId": "456",
                "score": 0.666
            }
        ]
        self.write(ujson.dumps(recommendation_list))
