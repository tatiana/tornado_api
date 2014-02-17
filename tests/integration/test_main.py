import json

from tornado.testing import AsyncHTTPTestCase

from lex import main


class HandlersTestCase(AsyncHTTPTestCase):

    def get_app(self):
        return main.application

    def test_healthcheck(self):
        response = self.fetch('/healthcheck', method='GET')
        self.assertEqual(response.code, 200)
        self.assertIn('Atchim!', response.body)

    def test_recommendation(self):
        config = {
            "userId": 1234,
            "userProvider": 2,
            "excludeIds": [123, 5235, 123],
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
                "documentId": "1233",
                "score": 0.999
            },
            {
                "documentId": "456",
                "score": 0.666
            }
        ]
        computed = json.loads(response.body)
        self.assertEqual(computed, expected)
