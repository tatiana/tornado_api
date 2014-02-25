import json

from mock import patch
from tornado.testing import AsyncHTTPTestCase

from lex import main


#TIMEOUT = 30


class HandlersTestCase(AsyncHTTPTestCase):

    def get_app(self):
        return main.application

    # def wait(self, condition=None, timeout=None):
    #     return super(HandlersTestCase, self).wait(None, TIMEOUT)

    def test_healthcheck(self):
        response = self.fetch('/healthcheck', method='GET')
        self.assertEqual(response.code, 200)
        self.assertEqual('Atchim!', response.body)

    def test_version(self):
        response = self.fetch('/version', method='GET')
        self.assertEqual(response.code, 200)
        values = response.body.split("|")
        self.assertEqual(len(values), 2)

    def test_root(self):
        response = self.fetch('/', method='GET')
        self.assertEqual(response.code, 200)
        expected = 'My name is Lex. Lex Luthor.<br>Learn how to use me by reading the <a href="/docs/">docs</a>.'
        self.assertEqual(response.body, expected)

    def test_docs(self):
        response = self.fetch('/docs/', method='GET')
        self.assertEqual(response.code, 200)
        self.assertIn('API for recommending news using content-based algorithms.', response.body)

    def test_recommendation_returns_200(self):
        config = {
            "userId": 1234,
            "userProvider": 2,
            "excludeIds": ["123", "5235", "123"],
            "dateStart": "1997-07-16T19:20:30.45+01:00",
            "dateEnd": "1997-07-16T19:20:30.45+01:00",
            "product": "mobile",
            "limit": 2
        }
        response = self.fetch(
            '/recommendation',
            method='POST',
            body=json.dumps(config)
        )
        self.assertEqual(response.code, 200)
        expected = [
            {
                "documentId": "6116038798098712381",
                "score": 0.999
            },
            {
                "documentId": "6502978799245377158",
                "score": 0.666
            },
            {
                "documentId": "5412347350701788586",
                "score": 0.333
            }
        ]
        response = json.loads(response.body)
        self.assertEqual(response, expected)

    def test_recommendation_returns_400(self):
        config = {
            "userId": 5678
        }
        response = self.fetch(
            '/recommendation',
            method='POST',
            body=json.dumps(config)
        )
        self.assertEqual(response.code, 400)
        response = json.loads(response.body)
        self.assertTrue("error" in response)

    @patch("lex.handlers.validate", side_effect=Exception)
    def test_recommendation_returns_500(self, mock_validate):
        config = {
            "userId": 5678
        }
        response = self.fetch(
            '/recommendation',
            method='POST',
            body=json.dumps(config)
        )
        self.assertEqual(response.code, 500)
        response = json.loads(response.body)
        self.assertTrue("error" in response)
