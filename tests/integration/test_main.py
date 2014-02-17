from tornado.testing import AsyncHTTPTestCase

from lex import main


class MainTestCase(AsyncHTTPTestCase):

    def get_app(self):
        return main.application

    def test_healthcheck(self):
        response = self.fetch('/healthcheck', method='GET')
        self.assertEqual(response.code, 200)
        self.assertIn('Atchim!', response.body)
