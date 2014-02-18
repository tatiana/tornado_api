import unittest

from lex import params


class ParamsTestCase(unittest.TestCase):

    def test_has_exception(self):
        self.assertTrue(params.ParamsException)

    def test_has_obligatory_keys(self):
        self.assertTrue(params.OBLIGATORY_KEYS)
        expected = [
            'dateStart',
            'product',
            'userId',
            'excludeIds',
            'dateEnd',
            'limit',
            'userProvider'
        ]
        self.assertEqual(params.OBLIGATORY_KEYS, expected)

    def test_validate_params_raises_exception(self):
        empty_params = {}
        with self.assertRaises(params.ParamsException) as exception:
            params.validate(empty_params)
        expected = "Expected the following keys: ['dateEnd', 'dateStart', 'excludeIds', 'limit', 'product', 'userId', 'userProvider'], but received: []"
        self.assertEqual(str(exception.exception), expected)

    def test_validate_params_succeeds(self):
        valid_params = {
            "userId": 1234,
            "userProvider": 2,
            "excludeIds": [123, 5235, 123],
            "dateStart": "1997-07-16T19:20:30.45+01:00",
            "dateEnd": "1997-07-16T19:20:30.45+01:00",
            "product": "mobile",
            "limit": 2
        }
        self.assertTrue(params.validate(valid_params))
