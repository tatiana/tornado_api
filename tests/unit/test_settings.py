import unittest

from lex import settings


class SettingsTestCase(unittest.TestCase):

    def test_local_values(self):
        self.assertEqual(settings.DEBUG, True)
        self.assertEqual(settings.CORS_HEADERS, 'Content-Type, Authorization')
        self.assertEqual(settings.SERVER_PORT, 8888)
