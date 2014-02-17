"""
Handlers for lex's API resources.
"""

from tornado.web import RequestHandler


class HealthcheckHandler(RequestHandler):
    """
    Return "Atchim!" if service is running.
    """

    def get(self):
        self.write("Atchim!")
